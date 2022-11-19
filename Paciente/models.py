from django.db import models

# Create your models here.
from django.db import models
#from UsuarioSesion.models import Comuna
#from Familiar_paciente.models import Familiar_pacienteM
#from UsuarioSesion.models import IniciaSesion

# Create your models here.
class Sintomas(models.Model):
    nombre_sintoma = models.CharField(max_length=50, help_text="Ingrese el nombre del sintoma")    
    def __str__(self):
        return f'{self.id}, {self.nombre_sintoma}'  


class Paciente(models.Model):
    sexo_biologico = models.CharField(max_length=20, help_text="Ingrese su sexo biologico")
    #usuario = models.ForeignKey(IniciaSesion, on_delete=models.CASCADE)
    #comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id}, {self.usuario}'  

class Patologia(models.Model):
    nombre_patologia = models.CharField(max_length=50, help_text="Ingrese el nombre de la patologia")
    
    def __str__(self):
        return f'{self.id}, {self.nombre_patologia}'  

class Ingreso(models.Model):
    fecha_ingreso = models.DateField(blank=True, help_text="Ingrese la fecha de ingreso")
    hora = models.DateTimeField(blank=True, help_text="Ingrese la hora de ingreso")
    cant_sintomas = models.PositiveIntegerField(help_text="Ingrese la cantidad de sintomas que presenta el paciente")
    #familiar_paciente = models.ForeignKey(Familiar_pacienteM, on_delete=models.CASCADE)
    #paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    #patologia = models.ForeignKey(Patologia, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}, {self.fecha_ingreso}'  


class SintomasPaciente(models.Model):
    descripcion_sintoma = models.CharField(max_length=50, help_text="Ingrese la descripcion del sintoma")
    #sintoma=models.ForeignKey(Sintomas, null=True, blank=True ,on_delete=models.CASCADE)
    #paciente=models.ForeignKey(Paciente, null=True ,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id}, {self.fecha_ingreso}'  

    class Meta:
        verbose_name = 'Sintomas_Paciente'
