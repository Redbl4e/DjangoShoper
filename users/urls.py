from django.urls import path

from users.views import  AuthenticationUser

app_name = 'users'

urlpatterns = [
    path('authentication/', AuthenticationUser.as_view(), name='register')
    # path('authorization')
]
