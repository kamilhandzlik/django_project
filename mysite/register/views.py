from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy

#
# # Create your views here.

# def register(response):
#     if response.method == "POST":
#         form = RegisterForm(response.POST)
#         if form.is_valid():
#             form.save()
#
#         return  redirect('/home')
#     else:
#         form = RegisterForm()
#
#     form = RegisterForm()
#     return render(response, 'register/register.html', {"form":form})


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register/register.html"
    success_url = reverse_lazy("home")


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "authentication/register.html"
    success_url = reverse_lazy("home")


class CustomLoginView(LoginView):
    template_name = "authentication/login.html"
    success_url = reverse_lazy("home")


class CustomLogoutView(LogoutView):
    pass
