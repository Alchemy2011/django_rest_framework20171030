from django.contrib.auth.models import User, Group
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from quickstart.models import Snippet
from quickstart.serializers import UserSerializer, GroupSerializer, SnippetSerializer


class UserViewSet(viewsets.ModelViewSet):
    """查看编辑用户的API接口"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """查看编辑分组的API接口"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# FIXME <不能用>
class SnippetViewSet(viewsets.ModelViewSet):
    """
    代码片段视图集，继承自框架的视图集的模型视图集
    """
    # 查询集自然就是所有模型对象，联想一下django中如何获取模型的所有对象
    queryset = Snippet.objects.all()
    # 特殊的是，需要制定序列化类
    serializer_class = SnippetSerializer
