# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
from rest_framework import serializers

from computerapp.models import Product, Category, Manufacturer


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'model', 'description', 'image', 'price',
                  'category', 'manufacturer', 'created', 'updated', )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', )


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'description',)


class ProductRetrieveSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Product
        fields = ('id', 'model', 'description', 'image', 'price',
                  'category', 'manufacturer', 'created', 'updated', )
