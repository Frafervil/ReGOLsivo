from django.db import models

# Create your models here.


class Usuario(models.Model):
    Nombre = models.CharField(max_length=35, null=False, blank=False)
    Apellidos = models.CharField(max_length=35, null=False, blank=False)
    Email = models.EmailField(max_length=35, null=False, blank=False)
    Karma = models.IntegerField(default=0, null=False, blank=False)