from django.db import models

# Create your models here.
class UsuariosBO(models.Model):
    usuario=models.CharField(max_length=40)
    contraseña=models.CharField(max_length=40)
    oblea=models.CharField(max_length=40)
    legajo=models.CharField(max_length=7)

