# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # 序列化器
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'first_name',
                  'last_name', 'date_joined', 'groups')
        # fields = ('username',)  可以删除显示的键
        # django已经帮你把groups和users的关系定义好了


# 直接从上面复制，减少出错
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    # 序列器
    class Meta:
        model = Group
        fields = ('id', 'url', 'name',)
        # url是为了生成链接
