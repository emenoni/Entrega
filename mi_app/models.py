from django.db import models

#Definimos cuáles son los tipos de datos que queremos grabar en nuestra base de datos

class familia(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()

class Juego(models.Model):
    nombre = models.CharField(max_length=30)
    max_jugadores = models.IntegerField()
    min_edad = models.IntegerField()

class Auto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    año = models.IntegerField()

