from abc import ABC

from rest_framework import serializers
from shop.models.сategory import Category, Product


class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "category")


class ShopSerializer(serializers.ModelSerializer):
    category_product = ExecutorSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ( 'category_product', 'name', 'description', 'price', 'in_stock')
