from rest_framework import serializers
from computerapp.models import Product, Category, Manufacturer, UserProfile, DeliveryAddress, Order

from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'mobile_phone', 'nickname', 'description',
                  'icon', 'created', 'updated',)
        read_only_fields = ('user',)


class UserInfoSerializer(serializers.ModelSerializer):
    profile_of = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
                  'date_joined', 'profile_of')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)
        # 只写，不显示密码
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        # 保存完用户后，还需要加用户档案，一对一，就在这里实现，注册新用户时，顺便创建用户档案
        user_profile = UserProfile(user=user)
        user_profile.save()
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'name',)


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'model', 'description', 'price', 'category',
                  'manufacturer', 'created', 'updated', 'image',)


class ProductRetrieveSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Product
        fields = (
        'id', 'model', 'description', 'price', 'category', 'manufacturer',
        'created', 'updated', 'image', 'sold',)


class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = ('id', 'user', 'contact_person', 'contact_mobile_phone',
                  'delivery_address', 'created', 'updated',)
        read_only_fields = ('user',)


class OrderListSerializer(serializers.ModelSerializer):
    # 如果没有这个，那么显示的字段将是id；使用了就全部返回
    product = ProductListSerializer()
    address = DeliveryAddressSerializer()

    class Meta:
        model = Order
        fields = ('id', 'status', 'user', 'product', 'price', 'quantity',
                  'remark', 'address', 'created', 'updated',)


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # 哪些让你改，哪些不让，是在序列器里实现的
        fields = ('id', 'user', 'product', 'price', 'quantity', 'remark',
                  'address', 'created', 'updated',)
        read_only_fields = ('user', 'price', 'address',)


class OrderRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id',)
