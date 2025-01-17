from django.db import models

# Create your models here.
class Tb_Usuario(models.Model):
    
  telefono = models.CharField(max_length=50)
  password = models.CharField(max_length=100)
  nombre = models.CharField(max_length=100)
  edad = models.IntegerField(default=18)
  apellidoMaterno = models.CharField(max_length=100)
  apellidoPaterno = models.CharField(max_length=100)
  status = models.BooleanField(default=1)

  objects = models.Manager()

  def __str__(self):
    return self.nombre 

class Tb_CatalogoServicio(models.Model):
    
  nombreServicio = models.IntegerField(default=0)
  status =  models.BooleanField(default=1)

  objects = models.Manager()

  def __str__(self):
    return self.nombreServicio

class tb_CalendarioServicio(models.Model):
    
  idUsuario = models.IntegerField(default=0)
  idServicio = models.IntegerField(default=0)
  latitud = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
  longitud = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
  domicilio = models.CharField(max_length=100, default="")
  status =  models.BooleanField(default=1)

  objects = models.Manager()

  def __str__(self):
    return self.domicilio