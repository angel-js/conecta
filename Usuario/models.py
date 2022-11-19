from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class IniciaSesion(models.Model):
    nombre = models.CharField(max_length=20, help_text="Ingrese sus nombres")
    apellido = models.CharField(max_length=40, help_text="Ingrese sus apellidos")
    rut = models.CharField( max_length=10, help_text="Ingrese su RUT sin puntos ni guión")
    contraseña = models.CharField(max_length=50, help_text="Ingrese su contraseña")
    fecha_nac = models.DateField(help_text="Ingrese su fecha de nacimiento")
    correo = models.EmailField(blank=True, help_text="Indique un correo válido")
    telefono = models.PositiveIntegerField( help_text="Ingrese el Numero de telefono")
    direccion = models.CharField(blank=True ,max_length=45, help_text="Ingrese su dirección (Calle y número)")
    funcionario = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}, {self.apellido}, {self.nombre}'  

    # Foreign keys de InicioSesion (Roles)

class Roles(models.Model):
    nombre_rol = models.CharField(max_length=20, help_text="Ingrese el nombre del Rol")
    lectura = models.BooleanField(default=False)
    Escritura = models.BooleanField(default=False)
    Edicion = models.BooleanField(default=False)
    Borrar = models.BooleanField(default=False)
    Crear = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}, {self.nombre_rol}'  


class Comuna(models.Model):
    nombre_comuna = models.CharField(max_length=50, help_text="Ingrese el nombre de la comuna")
    
    def __str__(self):
        return f'{self.id}, {self.nombre_comuna}'  
    
    # Foreign keys(Region)

class Region(models.Model):
    nombre_region = models.CharField(max_length=50, help_text="Ingrese el nombre de la Region")

    def __str__(self):
        return f'{self.id}, {self.nombre_region}'  