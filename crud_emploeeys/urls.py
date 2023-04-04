from django.urls import path

from crud_emploeeys.views import (ViewCRUD, CreateItemEmploeeys,
                                  ItemUpdateView, ItemDeleteView)

app_name = 'crud'

urlpatterns = [
    path('', ViewCRUD.as_view(), name='home'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    path('create/', CreateItemEmploeeys.as_view(), name='create'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete')
]
