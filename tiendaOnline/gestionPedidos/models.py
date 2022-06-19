from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre    = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email     = models.EmailField(max_length=30)
    tlf       = models.CharField(max_length=11)

class Articulo(models.Model):
    nombre    = models.CharField(max_length=30)
    precio    = models.IntegerField()

class Pedido(models.Model):
    numero    = models.IntegerField()
    fecha     = models.BooleanField()    
        