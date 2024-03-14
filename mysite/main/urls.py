# Tutaj dodaję ścieżki

from django.urls import path
from . import  views

urlpatterns = [
path("<str:name>", views.index, name="index"),
path("", views.home, name="home"),
path("create/", views.create, name="create"),
 # Pamiętaj wpisując url będziesz musiał użyć /ścieżka/
]