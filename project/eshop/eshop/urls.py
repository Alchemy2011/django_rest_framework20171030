"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^computer/', include('computerapp.urls')),  
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),  
    url(r'^api-token-auth/', views.obtain_auth_token),
    # 自动生成API文档：http://www.django-rest-framework.org/topics/documenting-your-api/
    url(r'^docs/', include_docs_urls(title='My API title')),
    # url(r'^docs/', include_docs_urls(title='My API title', public=False)),
    # 第三方包drfdocs的配置
    # https://github.com/manosim/django-rest-framework-docs
    # url(r'^docs/', include('rest_framework_docs.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








