from django.db import models


# Create your models here.
class Agenda (models.Model):
    nombre= models.CharField(max_length=20)
    apellido =  models.CharField(max_length=20)
    ci = models.CharField(max_length=50)
    nro_tel = models.CharField(max_length=10)
    correo = models.EmailField(unique=True)
    def __str__(self):
        return self.nombre
    