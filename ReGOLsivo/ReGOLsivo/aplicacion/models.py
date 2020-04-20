from django.db import models

# Create your models here.

class CuentaDeUsuario(models.Model):
    NombreDeUsuario = models.CharField(max_length=32, null=False, blank=False, unique=True)
    Contraseña = models.CharField(max_length=32, blank=False)

    def __str__(self):
        return self.NombreDeUsuario

class Actor(models.Model):
    Nombre = models.CharField(max_length=35, null=False, blank=False)
    Apellidos = models.CharField(max_length=35, null=False, blank=False)
    CuentaDeUsuario = models.ForeignKey(CuentaDeUsuario, null=False, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Usuario(Actor):
    Email = models.EmailField(max_length=35, null=False, blank=False)
    Karma = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return super().Nombre