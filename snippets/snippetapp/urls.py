# -*- coding: utf-8 -*-
# __author__ = 'liqirong'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippetapp import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail)
]
# 目的是实现最简单的在网址中切换json和api，
# 特别注意还需要在views中增加format=None这个参数
urlpatterns = format_suffix_patterns(urlpatterns)

# 第一级用法结束
# from django.conf.urls import url
# from snippetapp import views
#
# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]
