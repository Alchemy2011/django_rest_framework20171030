# -*- coding: utf-8 -*-
# __author__ = 'liqirong'


from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from video import views

urlpatterns = [
    url(r'^video_list/$', views.PostListView.as_view(), name='video_list'),
    url(r'^video_detail/(?P<pk>[\d]+)/$', views.PostDetailView.as_view(), name='video_detail'),
]
