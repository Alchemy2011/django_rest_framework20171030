from django.contrib.auth.models import User, Group
from django.shortcuts import render

from rest_framework import viewsets

from quickstart.serializers import UserSerializer, GroupSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    查看、编辑用户数据的API接口
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


# 代码重用，直接复制已经验证过的代码，不容易出错
class GroupViewSet(viewsets.ModelViewSet):
    """
    查看、编辑群组数据的API接口
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
