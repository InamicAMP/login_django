from django.db import models
from django.contrib.auth.models import User

class Aspirante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    clave_elector = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100, blank=True)
    correo_electronico = models.EmailField()
    celular = models.CharField(max_length=10)
    telefono_adicional = models.CharField(max_length=10)
    como_se_entero = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.primer_apellido}"