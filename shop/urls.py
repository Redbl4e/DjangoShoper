from django.urls import path
from shop.views import ShopViewHome

app_name = 'shop'

urlpatterns = [
    path('', ShopViewHome.as_view(), name='home'),
]