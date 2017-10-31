# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
from rest_framework import serializers

from snippetapp.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

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
#     # 该方法由rest框架提供
#     def create(self, validated_data):
#         """
#         创建
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         更新
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
