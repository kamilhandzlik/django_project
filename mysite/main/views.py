from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from django.shortcuts import render
from .forms import CreateNewList

# Create your views here.

def index(response, name):
    try:
        ls = ToDoList.objects.get(name=name)     # Zapytanie z metodą get
    except ToDoList.DoesNotExist:
        ls = None

    {"save":[""], "c1":["clicked"]}
    if response.method == "POST":
        if response.Post.get("save"):
            pass

    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        # Tworzenie nowej ToDoLidt
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]   #pamiętaj o dodaniu tutaj poprawnych nawiasów
            t = ToDoList(name=n)
            t.save()        #Zapisywanie nowej ToDoList jeśli jej nazwa jest poprawna

        return HttpResponseRedirect("/%i" "%t".id) # Przekierowanie do listy

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

