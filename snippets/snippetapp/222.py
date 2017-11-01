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
# 将经过从序列器的数据渲染为json格式，之后就能输出到前端
content = JSONRenderer().render(serializer.data)
content
from django.utils.six import BytesIO
# 模拟数据流
stream = BytesIO(content)
# 将从前端获取的数据，解析为json格式后，需要用序列器处理，验证有效性后保存
data = JSONParser().parse(stream)
serializer = SnippetSerializer(data=data)
serializer.is_valid()
serializer.validated_data
serializer.save()
# 只要使用all，就需要many=True
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
from snippetapp.serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer))
