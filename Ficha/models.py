from django.db import models

# Create your models here.
class FichaMedica(models.Model):
    fecha_creacion = models.DateTimeField()

    def __str__(self):
        return f'{self.id}'

# Foreign keys (ID Historial=Comentario) (ID Ingreso) 