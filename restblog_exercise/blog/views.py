from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions

from blog.models import Post


# 注意命名习惯，加个View，为了清晰，养成习惯
# 从PostListView到PostLCView，避免太长，取首字母，惯例
# 不知道引用的快捷方式，就从之前的项目直接粘贴
from blog.serializers import PostLCSerializer, PostRUDSerializer, PostListSerializer


class PostLCView(generics.ListCreateAPIView):
    """
    博文列表，创建新博文
    """
    # 有的时候，不想取全部，还有新方法
    queryset = Post.objects.all()
    serializer_class = PostLCSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class PostListView(generics.ListAPIView):
    """
    博文列表
    """
    # 有的时候，不想取全部，还有新方法
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    # permission_classes = (permissions.IsAuthenticated,)


# 最好找之前做过的RUD直接复制，因为如果从上边复制，随着功能的增多，差别会很大
# 这个视图和序列器相关，
class PostRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    博文RUD
    """
    queryset = Post.objects.all()
    serializer_class = PostRUDSerializer
    # permission_classes = (permissions.IsAuthenticated,)
