# -*- coding: utf-8 -*-
# __author__ = 'liqirong'


from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from blog import views

urlpatterns = format_suffix_patterns([
    # 注意命名方式，专业程序员blog_lc
    url(r'^post_lc/$', views.PostLCView.as_view(), name='post_lc'),
    # 方法一，做两个地址
    url(r'^post_list/$', views.PostListView.as_view(), name='post_list'),
    # 等会儿要用，先注释掉
    # 路由和视图相关，一步一步向前找
    url(r'^post_rud/(?P<pk>[\d]+)/$', views.PostRUDView.as_view(), name='post_rud'),
])
