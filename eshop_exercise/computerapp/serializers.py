# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
from rest_framework import serializers

from computerapp.models import Product


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        # fields = ('id', 'model', 'description', 'image', 'price',
        #           'category', 'manufacture', 'created', 'updated')
        exclude = ('sold', )
