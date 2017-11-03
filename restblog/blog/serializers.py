# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
from rest_framework import serializers

from blog.models import Post


# 复制后要检查
class PostLCSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        # 从models.py里复制
        fields = ('id', 'title', 'content', 'created', 'updated', 'category', 'tags')
