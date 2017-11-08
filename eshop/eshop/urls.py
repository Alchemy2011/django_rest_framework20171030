"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^computer/', include('computerapp.urls')),
    # http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
    # 这个接口就是给前端做登录的，前端会来问题，怎么用这个接口，
    # 身份验证不能用之前的方法，需要前端工程师在前端用js设置header，
    # 前端不会做的话，会来问你。
    url(r'^api-token-auth/', views.obtain_auth_token),
]

# https://docs.djangoproject.com/en/1.11/howto/static-files/ 媒体文件不显示
# 如果是调试模式
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
