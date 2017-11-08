# Create your views here.
from datetime import datetime

from rest_framework import generics
from rest_framework import permissions
from rest_framework.filters import OrderingFilter, SearchFilter

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.pagination import LimitOffsetPagination

from computerapp.models import Product, UserProfile, DeliveryAddress, Order

from computerapp.serializers import ProductListSerializer, ProductRetrieveSerializer, UserInfoSerializer, \
    UserProfileSerializer, UserSerializer, DeliveryAddressSerializer, OrderListSerializer, OrderCreateSerializer, \
    OrderRUDSerializer

from rest_framework.exceptions import NotFound

import logging

LOG_FILENAME = 'shop.log'

# logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)


class ProductListView(generics.ListAPIView):
    """
    产品列表
    """
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('description',)
    ordering_fields = ('category', 'manufacturer', 'created', 'sold', 'stock',)
    ordering = ('id',)
    pagination_class = LimitOffsetPagination


class ProductListByCategoryView(generics.ListAPIView):
    """
    产品按类别列表
    """
    serializer_class = ProductListSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('description',)
    ordering_fields = ('category', 'manufacturer', 'created', 'sold', 'stock', 'price',)
    ordering = ('id',)

    def get_queryset(self):

        category = self.request.query_params.get('category', None)

        if category is not None:
            queryset = Product.objects.filter(category=category)
        else:
            queryset = Product.objects.all()

        return queryset


class ProductListByCategoryManufacturerView(generics.ListAPIView):
    """
    产品按类别按品牌列表
    """
    serializer_class = ProductListSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('description',)
    ordering_fields = ('category', 'manufacturer', 'created', 'sold', 'stock', 'price',)
    ordering = ('id',)

    def get_queryset(self):

        category = self.request.query_params.get('category', None)
        manufacturer = self.request.query_params.get('manufacturer', None)

        if category is not None:
            queryset = Product.objects.filter(category=category, manufacturer=manufacturer, )
        else:
            queryset = Product.objects.all()

        return queryset


class ProductRetrieveView(generics.RetrieveAPIView):
    """
    产品详情
    """
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer
    permission_classes = (permissions.AllowAny,)


class UserInfoView(APIView):
    """
    用户基本信息
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        user = self.request.user
        serializer = UserInfoSerializer(user)
        return Response(serializer.data)


class UserProfileRUView(generics.RetrieveUpdateAPIView):
    """
    用户其他信息
    """
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        user = self.request.user

        obj = UserProfile.objects.get(user=user)

        return obj


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class DeliveryAddressLCView(generics.ListCreateAPIView):
    """
    收货地址LC
    """
    serializer_class = DeliveryAddressSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user

        queryset = DeliveryAddress.objects.filter(user=user)

        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        s = serializer.save(user=user)
        profile = user.profile_of
        profile.delivery_address = s
        profile.save()


class DeliveryAddressRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    收货地址RUD
    """
    serializer_class = DeliveryAddressSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # 获取单条数据用get_object，获取列表数据用get_queryset
    def get_object(self):
        user = self.request.user

        try:
            obj = DeliveryAddress.objects.get(id=self.kwargs['pk'], user=user)
        except Exception:
            raise NotFound('not found')

        return obj


class CartListView(generics.ListAPIView):
    """
    Cart List
    """
    serializer_class = OrderListSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user

        queryset = Order.objects.filter(user=user, status='0')

        return queryset


# 与上面的区别
class OrderListView(generics.ListAPIView):
    """
    Order List
    """
    serializer_class = OrderListSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user

        # 以什么为筛选标准
        queryset = Order.objects.filter(user=user, status__in=['1', '2', '3', '4'])

        return queryset


class OrderCreateView(generics.CreateAPIView):
    """
    Order Create
    """
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user

        # 获取序列器里经过验证的前端传来的数据
        product = serializer.validated_data.get('product')

        # 价格是根据产品id从数据库里获取，不从前端获取，防止前端乱改
        # 反向关联，知道用户查地址。
        serializer.save(user=user, price=product.price, address=self.request.user.profile_of.delivery_address)

        # logging.debug('this is debug')
        # logging.info('this is critical %s', 'added')
        # 电商的记录功能就在这里实现的
        logging.info('user %d cart changed, product %d related, Time is %s.',
                     user.id, product.id, str(datetime.now()))


class OrderRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    Order
    """
    serializer_class = OrderRUDSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        user = self.request.user

        obj = Order.objects.get(user=user, id=self.kwargs['pk'])

        return obj

    # 下单，只需要将status改成1
    def perform_update(self, serializer):
        user = self.request.user

        serializer.save(user=user, status='1')
