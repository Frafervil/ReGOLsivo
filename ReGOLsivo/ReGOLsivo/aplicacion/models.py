from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

import numpy as np

import pandas as pd
from joblib import dump, load

# Create your models here.

class Actor(AbstractUser):
    pass

class Usuario(Actor):
    karma = models.IntegerField(default=20, null=False, blank=False)

    def __str__(self):
        return super().username

class Administrador(Actor):

    def __str__(self):
        return super().username

class Logro(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    usuarios = models.ManyToManyField(Usuario)

    def __str__(self):
        return self.nombre

class Dificultad(models.TextChoices):
    Facil = 'Fácil'
    Intermedia = 'Intermedia'
    Dificil = 'Difícil'

class Partido(models.Model):
    nombreLocal = models.CharField(max_length=35, null=False, blank=False)
    nombreVisitante = models.CharField(max_length=35, null=False, blank=False)
    resultado = models.CharField(max_length=35, null=False, blank=False)
    hora = models.TimeField(null=False, blank=False)
    dia = models.DateField(null=False, blank=False)
    pronosticoSistema = models.CharField(max_length=35, null=False, blank=False)
    premio = models.PositiveIntegerField(null=False, blank=False)
    dificultad = models.CharField(max_length=35, choices=Dificultad.choices, null=False, blank=False)
    proporcion_de_puntos_del_equipo_local = models.DecimalField(max_digits=11, decimal_places=9, null=False, blank=False)
    proporcion_de_puntos_del_equipo_visitante = models.DecimalField(max_digits=11, decimal_places=9, null=False, blank=False)
    goles_por_partido_del_equipo_local = models.DecimalField(max_digits=11, decimal_places=9, null=False, blank=False)
    goles_por_partido_del_equipo_visitante = models.DecimalField(max_digits=11, decimal_places=9, null=False, blank=False)

    def calcular_pronostico(self):
        # Cargar el modelo
        clf = load('partidos_knn.joblib')

        # Crear un registro para un partido
        registro = np.array([self.proporcion_de_puntos_del_equipo_local, self.proporcion_de_puntos_del_equipo_visitante, self.goles_por_partido_del_equipo_local, self.goles_por_partido_del_equipo_visitante])

        # Obtener la predicción
        self.pronosticoSistema = clf.predict([registro])[0]

    def __str__(self):
        cadena = "{0} - {1}"
        return cadena.format(self.nombreLocal, self.nombreVisitante)

class Pronostico(models.Model):
    resultado = models.CharField(max_length=35, null=False, blank=False)
    acertado = models.BooleanField(default=False, null=False, blank=False)
    usuario = models.ForeignKey(Usuario, null=False, blank=True, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, null=False, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return  '%s --> %s'%(self.usuario.username, self.partido)

class Comentario(models.Model):
    momento = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    texto = models.TextField(null=False, blank=False)
    meGustas = models.PositiveIntegerField(default=0, null=False, blank=False)
    autor = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, null=False, on_delete=models.CASCADE)
    comentarioRespuesta = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s --> %s'%(self.autor.username, self.partido)

class Configuracion(models.Model):
    valorComentariosPositivos = models.PositiveIntegerField(default=50, null=False, blank=False)
    premioComentariosPositivos = models.PositiveIntegerField(default=100, null=False, blank=False)
