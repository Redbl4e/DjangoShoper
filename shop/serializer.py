from abc import ABC

from rest_framework import serializers

from shop.models.category import  Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "category")


class ShopSerializer(serializers.ModelSerializer):
    category_product = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('pk', 'category_product',  'name', 'description', 'price', 'in_stock', 'item_img')

