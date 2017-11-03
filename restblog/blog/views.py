from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions

from blog.models import Post


# 注意命名习惯，加个View，为了清晰，养成习惯
# 从PostListView到PostLCView，避免太长，取首字母，惯例
# 不知道引用的快捷方式，就从之前的项目直接粘贴
from blog.serializers import PostLCSerializer


class PostLCView(generics.ListCreateAPIView):
    """
    博文列表，创建新博文
    """
    # 有的时候，不想取全部，还有新方法
    queryset = Post.objects.all()
    serializer_class = PostLCSerializer
    permission_classes = (permissions.IsAuthenticated,)
