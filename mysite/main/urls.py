# Tutaj dodaję ścieżki

from django.urls import path
from . import  views

urlpatterns = [
path("", views.index, name="index"),
path("v1/", views.v1, name="view 1"), # Pamiętaj wpisując url będziesz musiał użyć /v1/
]