# Tutaj dodaję ścieżki

from django.urls import path
from . import  views

urlpatterns = [
path("<str:name>", views.index, name="index"),
 # Pamiętaj wpisując url będziesz musiał użyć /v1/
]