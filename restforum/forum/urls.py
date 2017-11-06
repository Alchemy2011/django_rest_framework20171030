# -*- coding: utf-8 -*-
# __author__ = 'liqirong'


from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from forum import views

# http://www.django-rest-framework.org/api-guide/format-suffixes/
urlpatterns = format_suffix_patterns([
    url(r'^topic_list/$', views.TopicListView.as_view(), name='topic_list'),
    url(r'^topic_retrieve/(?P<pk>[\d]+)/$', views.TopicRetrieveView.as_view(), name='topic_retrieve'),
    url(r'^comment_create/$', views.CommentCreateView.as_view(), name='comment_create'),
    url(r'^filter_url/(?P<username>.+)/$', views.FilterUrlListView.as_view(), name='filter_url'),
], allowed=['api', 'json', ])
# 把allowed想成白名单
