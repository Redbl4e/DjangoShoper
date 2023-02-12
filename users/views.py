from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView


class AuthenticationUser(LoginView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"

