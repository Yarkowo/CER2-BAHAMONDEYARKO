from django.db import models

# Create your models here.

class Entidad(models.Model):
    id = models.BigAutoField
    nombre = models.CharField
    logo = models.ImageField

class Comunicado(models.Model):
    id = models.BigAutoField
    titulo = models.CharField
    detalle = models.CharField
    detalle_corto = models.CharField
    tipo = models.TIPO_CHOICES
    entidad = models.Entidad
    visible = models.BooleanField
    fecha_publicacion = models.DateTimeField
    fecha_ultima_modificacion = models.DateTimeField
    publicado_por = models.User
    modificado_por = models.User

class TIPO_CHOICES(models.enums):[
    ("S","Suspensión de actividades"),
    ("C","Suspensión de clase"),
    ("T","Información")]
