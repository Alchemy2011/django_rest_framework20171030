# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippetapp import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[\d]+)/$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[\d]+)/$', views.UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

# # 特别注意：下面需要使用方括号，如果误操作为花括号，就会报错
# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
#
# from snippetapp import views
#
# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[\d]+)/$', views.snippet_detail),
# ]
#
# # http://www.django-rest-framework.org/api-guide/format-suffixes/
# # 如果想要限定哪些后缀，可以加上allowed参数 allowed=['json', 'api']，没有该参数，任何后缀均可
# # urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
# urlpatterns = format_suffix_patterns(urlpatterns)
