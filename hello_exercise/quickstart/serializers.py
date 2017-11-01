# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from quickstart.models import Snippet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # 序列器
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'first_name',
                  'last_name', 'date_joined', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name', 'user_set')


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
