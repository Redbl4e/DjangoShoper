import time

from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from users.forms import AuthorizationForm, UserCreationForm

user = get_user_model()


class RegistrationView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            pass


class LoginView(DjangoLoginView):
    form_class = AuthorizationForm

    def get_success_url(self):
        time.sleep(3)
        return reverse_lazy('shop:home')


class LogoutView(DjangoLogoutView):
    template_name = "home.html"
