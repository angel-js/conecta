from django.db import models

# Create your models here.
class Comentario(models.Model):
    estado = models.CharField(max_length=20, help_text="Ingrese el estado del Paciente")
    comentario = models.CharField(max_length=300, help_text="Ingrese el comentario")
    fecha_comentario = models.DateTimeField() 

    def __str__(self):
        return f'{Comentario.id}'

# Foreng Keys ID Funcionario  