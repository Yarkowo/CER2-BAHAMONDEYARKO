from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    logo = models.ImageField()
    def __str__(self):
        return self.nombre

class Comunicado(models.Model):

    TIPO_CHOICES=[("S","Suspensión de actividades"),
    ("C","Suspensión de clase"),
    ("T","Información")]

    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    detalle = models.TextField(max_length=120)
    detalle_corto = models.TextField(max_length=60)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True)
    modificado_por = models.ForeignKey(User, related_name="modificado_por", on_delete=models.CASCADE, editable=False, null=True)
    def __str__(self):
        return self.titulo


