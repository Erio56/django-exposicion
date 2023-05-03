from django.db import models

# Create your models here.

class Pelicula(models.Model):
   nombre_pelicula = models.CharField(max_length=200)
   calificacion = models.IntegerField()