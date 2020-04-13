from django.db import models

# Create your models here.

class Actor(models.Model):
    Nombre = models.CharField
    Apellidos = models.CharField


class Usuario(Actor):
    Email = models.EmailField
    Karma = models.IntegerField

    def NombreCompleto(self):
        cadena="{0}, {1}"
        return cadena.format(Actor.Nombre, Actor.Apellidos)

    def __str__(self):
        return Usuario.NombreCompleto()


class Administrador(Actor):
    Email = models.EmailField()

    def NombreCompleto(self):
        cadena="{0}, {1}"
        return cadena.format(Actor.Nombre, Actor.Apellidos)

    def __str__(self):
        return Administrador.NombreCompleto()

class Pronostico(models.Model):
    Resultado = models.CharField
    Acertado = models.BooleanField(default=False)
    Usuario = models.ForeignKey(Usuario, null=False, blank=True, on_delete=models.CASCADE)
    Partido = models.ForeignKey(Partido, null=False, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        cadena = "{2} => {3}"
        return cadena.format(self.Usuario, self.Partido)

class Partido(models.Model):
    NombreLocal = models.CharField
    NombreVisitante = models.CharField
    Resultado = models.CharField
    PronosticoSistema = models.CharField
    Premio = models.PositiveIntegerField
    Dificultad = models.CharField

    def __str__(self):
        cadena = "{0} - {1}"
        return cadena.format(self.NombreLocal, self.NombreVisitante)

class Comentario(models.Model):
    Autor = models.CharField
    Momento = models.DateTimeField(auto_now_add=True)
    Texto = models.CharField
    MeGustas = models.PositiveIntegerField
    Actor = models.ForeignKey(Actor, null=False, blank=True, on_delete=models.CASCADE)
    Partido = models.ForeignKey(Partido, null=False, blank=True, on_delete=models.CASCADE)