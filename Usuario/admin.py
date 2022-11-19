from .models import IniciaSesion
from django.contrib import admin

# Register your models here.
class iniciaSesionAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'apellido', 'correo')
    list_filter = ('id', 'correo')

admin.site.register(IniciaSesion, iniciaSesionAdmin)