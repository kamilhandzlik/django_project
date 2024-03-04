from django.db import models

# tutaj tworzysz modele dla bazy danych
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Ta klasa dziedziczy po klasie ToDoList
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField

    def __str__(self):
        return self.text

# po zrobieniu modeli trzeba mykonać migracje