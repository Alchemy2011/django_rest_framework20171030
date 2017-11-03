# -*- coding: utf-8 -*-
# __author__ = 'liqirong'


from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from blog import views

urlpatterns = format_suffix_patterns([
    # 注意命名方式，专业程序员blog_lc
    url(r'^post_lc/$', views.PostLCView.as_view(), name='post_lc'),
    # 等会儿要用，先注释掉
    # url(r'^users/(?P<pk>[\d]+)/$', views.UserDetail.as_view(), name='user-detail'),
])
