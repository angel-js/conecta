from django.db import models

# Create your models here.
class FuncionarioM(models.Model):
    cargo = models.CharField(max_length=40, help_text="Ingrese el cargo del funcionario")
    
    def __str__(self):
        return f'{self.id}, {self.cargo}'  

    # Foreign keys (Rol)(Usuario)(Comuna)