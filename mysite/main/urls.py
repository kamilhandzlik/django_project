# Tutaj dodaję ścieżki

from django.urls import path
from . import  views

urlpatterns = [
path("<str:name>", views.index, name="index"),
path("", views.home, name="home"),
 # Pamiętaj wpisując url będziesz musiał użyć /ścieżka/
]