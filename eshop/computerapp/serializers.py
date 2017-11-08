# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
from django.contrib.auth.models import User
from rest_framework import serializers

from computerapp.models import Product, Category, Manufacturer, UserProfile, DeliveryAddress


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


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'mobile_phone', 'nickname', 'description',
                  'icon', 'created',  'updated', 'delivery_address',)
        read_only_fields = ('user', )


class UserInfoSerializer(serializers.ModelSerializer):
    profile_of = UserProfileSerializer()

    class Meta:
        model = User
        # 字段从数据库里可以查看
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'profile_of', )


class DeliveryAddressLCSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryAddress
        fields = ('id', 'user', 'contact_person', 'contact_mobile_phone', 'delivery_address',
                  'created', 'updated',)
        # 下面这行代码没有意义，只不过比较清楚
        read_only_fields = ('user', )
