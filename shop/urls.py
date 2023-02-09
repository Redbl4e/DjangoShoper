from django.urls import path
from shop.views import ShopApiView


app_name = 'shop'

urlpatterns = [
    path('api/shop/', ShopApiView.as_view(), name='home'),
]