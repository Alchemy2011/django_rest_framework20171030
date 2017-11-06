# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
from django.contrib.auth.models import User
from rest_framework import serializers

from forum.models import Topic, Comment


class TopicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('id', 'content', 'user', 'created', )


class TopicRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('id', 'content', 'user', 'created', 'updated', )


# http://www.django-rest-framework.org/api-guide/serializers/
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', )


class CommentCreateSerializer(serializers.ModelSerializer):
    # http://www.django-rest-framework.org/api-guide/relations/
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created', 'updated', 'topic', 'user',)
        # http://www.django-rest-framework.org/topics/3.0-announcement/
        # read_only_fields = ('user', )  旧的方式，还能用
