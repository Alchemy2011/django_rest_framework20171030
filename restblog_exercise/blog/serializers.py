# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
from rest_framework import serializers

from blog.models import Post, Category, Tag


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        # 这是一个技巧，不知道加不加逗号，加一个逗号
        fields = ('id', 'name', )


# 复制后要检查
class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', )


class PostLCSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        # 从models.py里复制
        fields = ('id', 'title', 'content', 'created', 'updated', 'category', 'tags')


class PostListSerializer(serializers.ModelSerializer):
    # 让默认显示的id，显示的更丰富，以后都用这种方式
    # 显示关联的表的字段的方式
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created', 'updated', 'category', 'tags')


class PostRUDSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created', 'updated', 'category', 'tags')
        # read_only_fields = ('category', 'tags', )  # 这种老方法不行了，版本问题
        # 如果改标签，需要做另外的序列器
