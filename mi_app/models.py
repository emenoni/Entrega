from django.db import models

class familia(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()

