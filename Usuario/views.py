from django.shortcuts import render
from .models import IniciaSesion
from django.views import generic

# Create your views here.
def iniciarSesion(request):
    return render(request,'iniciasesion.html')

class SesionListView(generic.ListView):
    model = IniciaSesion