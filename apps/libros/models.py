from django.db import models

# Create your models here.

class Libros(models.Model):
    autor = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    categoria = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre
        
