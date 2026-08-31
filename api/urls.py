from django.urls import path
from .views import hello_world
from .views import usuarios

urlpatterns = [
    path("hello/", hello_world),
    path("usuarios/", usuarios),
]