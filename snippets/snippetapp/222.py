# -*- coding: utf-8 -*-
# __author__ = 'liqirong'

# 理解输入流程和输入流程时候用的，一般用不到命令提示行
from snippetapp.models import Snippet
from snippetapp.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
snippet = Snippet(code='helloworld')
snippet.save()
Snippet.objects.all()
serializer = SnippetSerializer(snippet)
serializer.data
content = JSONRenderer().render(serializer.data)
content
from django.utils.six import BytesIO
stream = BytesIO(content)
data = JSONParser().parse(stream)
serializer = SnippetSerializer(data=data)
serializer.is_valid()
serializer.validated_data
serializer.save()
# 只要使用all，就需要many=True
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
