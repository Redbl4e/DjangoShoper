import time
from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import AuthorizationForm, UserCreationForm

user = get_user_model()


class RegistrationView(CreateView):
    model = user
    form_class = UserCreationForm
    template_name = 'registration/registration.html'

    """Авторизация на сайте сразу после регистрации """
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('shop:home')


class LoginView(DjangoLoginView):
    form_class = AuthorizationForm

    def get_success_url(self):
        time.sleep(3)
        return reverse_lazy('shop:home')


class LogoutView(DjangoLogoutView):
    template_name = "home.html"
