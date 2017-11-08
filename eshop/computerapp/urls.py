# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from computerapp import views

# http://www.django-rest-framework.org/api-guide/format-suffixes/
urlpatterns = format_suffix_patterns([
    url(r'^product_list/$', views.ProductListView.as_view(), name='product_list'),
    url(r'^product_list_by_category/$', views.ProductListByCategoryView.as_view(),
        name='product_list_by_category'),
    url(r'^product_list_by_category_manufacturer/$', views.ProductListByCategoryManufacturerView.as_view(),
        name='product_list_by_category_manufacturer'),
    url(r'^product_retrieve/(?P<pk>[\d]+)/$', views.ProductRetrieveView.as_view(), name='product_retrieve'),
    url(r'^user_info/$', views.UserInfoView.as_view(), name='user_info'),
    url(r'^user_profile_ru/(?P<pk>[\d]+)/$', views.UserProfileRUView.as_view(), name='user_profile_ru'),
    url(r'^delivery_address_lc/$', views.DeliveryAddressLCView.as_view(), name='delivery_address_lc'),
], allowed=['api', 'json', ])
