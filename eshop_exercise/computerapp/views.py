from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from computerapp.models import Product
from computerapp.serializers import ProductListSerializer


class ProductListView(generics.ListAPIView):
    """
    话题列表
    """
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    # FIXME <刚修改完url，这里还没有处理>
    # http://www.django-rest-framework.org/api-guide/filtering/#orderingfilter
    # http://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    # 使用哪个过滤器，不知道，下面括号里的顺序决定了后端可视化页面上显示的顺序
    # 新功能，搜索、过滤功能，rest框架帮你搜了，用到哪个过滤器，就加哪个
    filter_backends = (SearchFilter, OrderingFilter, )  # 过滤器与哪个字段有关系
    # 经常是多个筛选条件
    # 下面的关键字，如果想改，需要定制，去看官方文档api
    ordering_fields = ('user', 'id', 'created',)  # 用来排序的字段，根据选择排序
    ordering = ('-id', )  # 与上面ordering_fields的区别是，默认排序
    # 前端看到的url是这样：http://127.0.0.1:8002/forum/topic_list/?search=金鱼
    search_fields = ('content', )  # 告诉你到哪个字段搜索
