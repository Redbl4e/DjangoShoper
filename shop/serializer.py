from abc import ABC

from rest_framework import serializers
from shop.models.сategory import Category, Product, MediaItem


class ItemImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaItem
        fields = ("id", "item_img")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "category")


class ShopSerializer(serializers.ModelSerializer):
    category_product = CategorySerializer(read_only=True)
    product_item_img = ItemImgSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('product_item_img', 'category_product',  'name', 'description', 'price', 'in_stock')

