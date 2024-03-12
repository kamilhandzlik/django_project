from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from django.shortcuts import get_object_or_404

# Create your views here.

def index(response, name):
    ls = ToDoList.objects.get(id=id)     # Zapytanie z metodą get
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})
