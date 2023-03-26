from django.urls import path
from shop.views import ShopApiView, ShopMensTitle, ShopMensTiTleShoes, ShopMensTiTleDjins

app_name = 'shop'

urlpatterns = [
    path('', ShopApiView.as_view(), name='home'),
    path('mens/title', ShopMensTitle.as_view(), name='menstitle'),
    path('mens/title/shoes', ShopMensTiTleShoes.as_view(), name='menstitleshoes'),
    path('mens/title/djins', ShopMensTiTleDjins.as_view(), name='menstitledjins')
]