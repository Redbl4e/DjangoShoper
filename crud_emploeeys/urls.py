from django.urls import path, include

from crud_emploeeys.views import ViewCRUD, CreateItemEmploeeys

app_name = 'crud'

urlpatterns = [
    path('', ViewCRUD.as_view(), name='home'),
    path('create/', CreateItemEmploeeys.as_view(), name='create')
]
