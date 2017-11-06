from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from forum.models import Topic, Comment
# http://www.django-rest-framework.org/
from django_filters.rest_framework import DjangoFilterBackend  # 这个需要安装，从api里找，其实这里并没有用到
from forum.serializers import TopicListSerializer, TopicRetrieveSerializer, CommentCreateSerializer


class TopicListView(generics.ListAPIView):
    """
    话题列表
    """
    queryset = Topic.objects.all()
    serializer_class = TopicListSerializer

    # http://www.django-rest-framework.org/api-guide/filtering/#orderingfilter
    # http://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    # 使用哪个过滤器，不知道，下面括号里的顺序决定了后端可视化页面上显示的顺序
    # 新功能，搜索、过滤功能，rest框架帮你搜了，用到哪个过滤器，就加哪个
    filter_backends = (SearchFilter, OrderingFilter, )  # 过滤器与哪个字段有关系
    # 经常是多个筛选条件
    # 下面的关键字，如果想改，需要定制，去看官方文档api
    ordering_fields = ('user', 'id', 'created',)  # 用来排序的字段，根据选择排序
    ordering = ('-id', )  # 与上面ordering_fields的区别是，默认排序
    # 前端看到的url是这样：http://127.0.0.1:8002/forum/topic_list/?search=金鱼
    search_fields = ('content', )  # 告诉你到哪个字段搜索


class TopicRetrieveView(generics.RetrieveAPIView):
    """
    话题Retrieve
    """
    # 详情的序列器，一般返回的多一点
    queryset = Topic.objects.all()
    # 可以和列表用同样的序列器，但一般不这样操作
    serializer_class = TopicRetrieveSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class CommentCreateView(generics.CreateAPIView):
    """
    评论创建
    """
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = (permissions.AllowAny, )

    # # 用来实现防止前端作弊的，就是谁登录就是谁，防止伪造用户
    # def perform_create(self, serializer):
    #     # 括号里就是，加的条件，不能让前端指定了，我们后端来指定
    #     serializer.save(user=self.request.user)
    # 问题是，不登录，还可以伪造；不给你传，你就伪造不了了
    def perform_create(self, serializer):
        # 匿名用户，返回True，匿名的用户和注册用户是两类用户
        # 这里判断条件是什么，不清楚，没有提示
        if self.request.user.is_anonymous():
            serializer.save()
        else:
            serializer.save(user=self.request.user)


# STEP <新功能，根据前端传来的用户名筛选，关键是如果获取url中提取出来的参数>
# http://www.django-rest-framework.org/api-guide/filtering/#filtering-against-the-url
class FilterUrlListView(generics.ListAPIView):
    """
    Filtering against the URL  对URL进行过滤
    """
    serializer_class = TopicListSerializer

    # 取出前端传来数据的方法
    def get_queryset(self):
        """
        This view should return a list of all the topics for
        the user as determined by the username portion of the URL.
        """
        # kwargs['username']和urls.py中(?P<username>.+)的一致
        username = self.kwargs['username']
        # 双下划线注意，以什么味筛选条件，在哪筛选
        return Topic.objects.filter(user__username=username)
