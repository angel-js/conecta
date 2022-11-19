from django.urls import path
from . import views

urlpatterns = [
    path('sesion', views.SesionListView.as_view(), name='iniciaSesion'),
]