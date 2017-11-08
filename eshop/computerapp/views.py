# Create your views here.
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from computerapp.models import Product, UserProfile, DeliveryAddress
from computerapp.serializers import ProductListSerializer, ProductRetrieveSerializer, UserInfoSerializer, \
    UserProfileSerializer, DeliveryAddressLCSerializer


class ProductListView(generics.ListAPIView):
    """
    产品列表
    """
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    # http://www.django-rest-framework.org/api-guide/filtering/#orderingfilter
    # http://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    # 使用哪个过滤器，不知道，下面括号里的顺序决定了后端可视化页面上显示的顺序
    # 新功能，搜索、过滤功能，rest框架帮你搜了，用到哪个过滤器，就加哪个
    filter_backends = (SearchFilter, OrderingFilter, )  # 过滤器与哪个字段有关系
    # 经常是多个筛选条件
    # 下面的关键字，如果想改，需要定制，去看官方文档api

    # 再往下做，不太容易，先注释掉
    ordering_fields = ('updated', 'created', 'price', 'sold')  # 用来排序的字段，根据选择排序
    # 像这种没出现在上面的字段，也可以像ordering_fields一样访问
    ordering = ('-sold', )  # 与上面ordering_fields的区别是，默认排序
    # 前端看到的url是这样：http://127.0.0.1:8002/forum/topic_list/?search=金鱼
    search_fields = ('model', 'description',)  # 告诉你到哪个字段搜索
    # http://www.django-rest-framework.org/api-guide/pagination/#limitoffsetpagination
    # 为了让前端控制每页返回的数量
    # 用法：http://127.0.0.1:8000/computerapp/product_list/?limit=3&offset=9
    pagination_class = LimitOffsetPagination


class ProductListByCategoryView(generics.ListAPIView):
    """
    产品按类别列表
    """
    serializer_class = ProductListSerializer
    filter_backends = (SearchFilter, OrderingFilter,)
    ordering_fields = ('updated', 'created', 'price', 'sold')
    ordering = ('-sold', )
    search_fields = ('model', 'description',)

    # 自定义获取查询集
    def get_queryset(self):
        # 从请求中获取查询参数http://127.0.0.1:8001/computer/product_list_by_category/?category=1
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
    filter_backends = (SearchFilter, OrderingFilter,)
    ordering_fields = ('updated', 'created', 'price', 'sold')
    ordering = ('-sold', )
    search_fields = ('model', 'description',)

    # 自定义获取查询集
    def get_queryset(self):
        # 从请求中获取查询参数http://127.0.0.1:8001/computer/product_list_by_category/?category=1
        category = self.request.query_params.get('category', None)
        manufacturer = self.request.query_params.get('manufacturer', None)
        if category is not None:
            queryset = Product.objects.filter(category=category, manufacturer=manufacturer)
        else:
            queryset = Product.objects.all()
        return queryset


class ProductRetrieveView(generics.RetrieveAPIView):
    """
    产品详情
    """
    queryset = Product.objects.all()
    # 一般来说详情使用的序列器字段多一点，所以和列表使用的序列器分开
    serializer_class = ProductRetrieveSerializer


# http://www.django-rest-framework.org/api-guide/views/
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
    # 没有差别的话，就用现成的，有特殊要求，再修改序列器
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # 新方法，不希望获取所用户的信息
    def get_object(self):
        user = self.request.user
        obj = UserProfile.objects.get(user=user)
        return obj


class DeliveryAddressLCView(generics.ListCreateAPIView):
    """
    收获地址LC
    """
    serializer_class = DeliveryAddressLCSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # 不能让查询所有的用户地址，当前用户只能看你自己的，不能看别人的
    def get_queryset(self):
        user = self.request.user
        queryset = DeliveryAddress.objects.filter(user=user)
        return queryset

    # 防作弊，也可以在序列器里面使用create，暂时不会
    # http://www.django-rest-framework.org/api-guide/generic-views/
    def perform_create(self, serializer):
        user = self.request.user
        s = serializer.save(user=user)  # 地址序列器，当然得到的是地址信息

        # 下面的代码是设置用户的默认地址
        profile = user.profile_of
        profile.delivery_address = s
        profile.save()
