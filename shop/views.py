
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models.category import Category
from shop.services.context import context_filter


class ShopApiView(APIView):
    def get(self, request):
        return render(request, 'home.html')


class ShopMensTitle(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        context = {
            "product": queryset
        }
        return render(request, 'item_shop/mens_title.html', context)


class ShopMensTiTleShoes(APIView):
    def get(self, request, **kwargs):
        context = context_filter(category_product_id=1, in_stock=True)
        return render(request, 'item_shop/mens_title_item.html', context)
        # return Response(context)

class ShopMensTiTleDjins(APIView):
    def get(self, request, **kwargs):
        context = context_filter(category_product_id=2, in_stock=True)
        return render(request, 'item_shop/mens_title_item.html', context)



