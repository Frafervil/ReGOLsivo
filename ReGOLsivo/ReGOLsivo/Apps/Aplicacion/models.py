from django.db import models

# Create your models here.

class Actor(models.Model):
    Nombre = models.CharField(max_length=35)
    Apellidos = models.CharField(max_length=35)


class Usuario(Actor):
    Email = models.EmailField
    Karma = models.IntegerField

    def NombreCompleto(self):
        cadena="{0}, {1}"
        return cadena.format(Actor.Nombre, Actor.Apellidos)

    def __str__(self):
        return Usuario.NombreCompleto(self)


class Administrador(Actor):
    Email = models.EmailField

    def NombreCompleto(self):
        cadena="{0}, {1}"
        return cadena.format(Actor.Nombre, Actor.Apellidos)

    def __str__(self):
        return Administrador.NombreCompleto(self)

class Partido(models.Model):
    NombreLocal = models.CharField(max_length=35)
    NombreVisitante = models.CharField(max_length=35)
    Resultado = models.CharField(max_length=35)
    PronosticoSistema = models.CharField(max_length=35)
    Premio = models.PositiveIntegerField
    Dificultad = models.CharField(max_length=35)

    def __str__(self):
        cadena = "{0} - {1}"
        return cadena.format(self.NombreLocal, self.NombreVisitante)

class Pronostico(models.Model):
    Resultado = models.CharField(max_length=35)
    Acertado = models.BooleanField(default=False)
    Usuario = models.ForeignKey(Usuario, null=False, blank=True, on_delete=models.CASCADE)
    Partido = models.ForeignKey(Partido, null=False, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        cadena = "{2} => {3}"
        return cadena.format(self.Usuario, self.Partido)

class Comentario(models.Model):
    Autor = models.CharField(max_length=35)
    Momento = models.DateTimeField(auto_now_add=True)
    Texto = models.CharField(max_length=35)
    MeGustas = models.PositiveIntegerField
    Actor = models.ForeignKey(Actor, null=False, blank=True, on_delete=models.CASCADE)
    Partido = models.ForeignKey(Partido, null=False, blank=True, on_delete=models.CASCADE)