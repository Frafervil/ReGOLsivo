from django.db import models

# Create your models here.


class CuentaDeUsuario(models.Model):
    nombreDeUsuario = models.CharField(max_length=32, null=False, blank=False, unique=True)
    contrasena = models.CharField(max_length=32, blank=False)

    def __str__(self):
        return self.nombreDeUsuario

class Actor(models.Model):
    nombre = models.CharField(max_length=35, null=False, blank=False)
    apellidos = models.CharField(max_length=35, null=False, blank=False)
    cuentaDeUsuario = models.ForeignKey(CuentaDeUsuario, null=False, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Usuario(Actor):
    email = models.EmailField(max_length=35, null=False, blank=False)
    karma = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return super().nombre

class Administrador(Actor):
    email = models.EmailField(max_length=35, null=False, blank=False)

    def __str__(self):
        return super().nombre

class Partido(models.Model):
    nombreLocal = models.CharField(max_length=35, null=False, blank=False)
    nombreVisitante = models.CharField(max_length=35, null=False, blank=False)
    resultado = models.CharField(max_length=35, null=False, blank=False)
    pronosticoSistema = models.CharField(max_length=35, null=False, blank=False)
    premio = models.PositiveIntegerField(null=False, blank=False)
    dificultad = models.CharField(max_length=35, null=False, blank=False)

    def __str__(self):
        cadena = "{0} - {1}"
        return cadena.format(self.nombreLocal, self.nombreVisitante)

class Pronostico(models.Model):
    resultado = models.CharField(max_length=35, null=False, blank=False)
    acertado = models.BooleanField(default=False, null=False, blank=False)
    usuario = models.ForeignKey(Usuario, null=False, blank=True, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, null=False, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        cadena = "{2} => {3}"
        return cadena.format(self.usuario, self.partido)

class Comentario(models.Model):
    autor = models.CharField(max_length=35, null=False, blank=False)
    momento = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    texto = models.CharField(max_length=35, null=False, blank=False)
    meGustas = models.PositiveIntegerField(null=False, blank=False)
    #actor = models.ForeignKey(Actor, null=False, blank=True, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, null=False, blank=True, on_delete=models.CASCADE)

class Configuracion(models.Model):
    mensajeBienvenidaIn = models.CharField(max_length=60, null=False)
    mensajeBienvenidaEs = models.CharField(max_length=60, null=False)
    linkLogo = models.URLField(max_length=200, null=False)
    valorComentariosPositivos = models.PositiveIntegerField(default=50, null=False, blank=False)
    valorComentariosPositivos = models.PositiveIntegerField(default=100, null=False, blank=False)