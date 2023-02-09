from abc import ABC

from rest_framework import serializers
from shop.models.сategory import Category, Product


class ChoicesProductSerializerField(serializers.SerializerMethodField, ABC):
    def to_representation(self, value):
        method_name = f'get_{Category.category}_display'
        method = getattr(value, method_name)
        return method()


class ShopSerializer(serializers.ModelSerializer):
    category_product = ChoicesProductSerializerField()

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'in_stock', 'category_product')
