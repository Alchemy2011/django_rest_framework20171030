# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
from rest_framework import serializers

from snippetapp.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

# 很少使用的第一级结束
# from rest_framework import serializers
#
# from snippetapp.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet
# # 与模型里的字段一一对应，这种方式不常用，修改密码的时候会用，
# # 常用ModelSerializer
# # 极像django的表单就是验证前端的输入，但不一样，是序列器里的字段
# # 另一个功能输出
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})  # 会显示一个文本框，不常用
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     # FIXME <不能显示链接，也不能修改>
#
#     # 该方法由rest框架提供，第二个参数是通过验证的数据
#     # 如何利用模型创建数据不会吗，这是底层的东西
#     def create(self, validated_data):
#         """
#         创建
#         """
#         # 这里有点技巧，通过验证的数据是json格式，需要解包**
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         更新
#         """
#         # 更新数据，如果外部通过验证的数据提供了，那么就用提供的，
#         # 如果外部没有提供，那么就继续用原来实例对象的数据值就可以了，
#         # 终于明白了，更新数据就是通过对新的通过验证的数据，
#         # 使用字典的get方法后，赋值给原有的数据实例对象，这个语法值得学习
#         # 通过验证的数据，和对象实例，都是从数据库中来的，所以格式一样
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
