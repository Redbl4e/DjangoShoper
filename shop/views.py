from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from shop.models.сategory import Product
from shop.serializer import ShopSerializer

# class ShopApiView(APIView):
#     def __init__(self, **kwargs):
#         super().__init__()
#         self.context = {}
#
#     def setup(self, request, *args, **kwargs):
#         super().setup(self, request, args, kwargs)
#         queryset = Product.objects.all()
#         serializer = ShopSerializer(queryset, many=True).data
#         self.context = {
#             "product": serializer
#         }
#
#     def get(self, request):
#         return Response(self.context)



class ShopViewHome(View):
    def get(self, request):
        return render(request, 'home.html')
