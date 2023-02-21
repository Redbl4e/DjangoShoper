from django.urls import path, include

from users.views import LogoutView, LoginView, RegistrationView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('', include('django.contrib.auth.urls'))
]
