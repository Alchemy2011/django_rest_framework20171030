# 从哪继承，想不到，想想需要实现什么功能
# 从通用类继承，想想第一天的例子
# 第四级
from django.contrib.auth.models import User
from rest_framework import generics, permissions

from snippetapp.models import Snippet
from snippetapp.serializers import SnippetSerializer, UserSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # 传过来一个序列器，就能在后端增加东西，防止前端作弊了
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 第三级结束
# from django.http import Http404
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from snippetapp.models import Snippet
# from snippetapp.serializers import SnippetSerializer
#
#
# class SnippetList(APIView):
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         # many=True不能丢
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class SnippetDetail(APIView):
#     def get_object(self, pk, format=None):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# 第二级结束
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from snippetapp.models import Snippet
# from snippetapp.serializers import SnippetSerializer
#
#
# # 这个装饰器作用很大
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     """
#     LC
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         # 这种Response会经常用到，这是rest_framework的正统响应，
#         # 比JSONResponse兼容性好，自动判断返回哪种格式，
#         # 内容协商前端想要什么格式，就返回什么格式
#         # 一个Response接口既能返回JsonResponse，又能返回HttpResponse
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         # api_view装饰器帮你解析了
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # 显式优于隐式
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # 注意：是返回序列器的错误，而不是原始的请求数据
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     """
#     RUD
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         # 对象不存在，只返回状态码就可以了
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         # 这里需要注意：由于是修改，所以序列器既需要数据库的数据，也需要请求的数据
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         # 对象有没有自带的删除方法，没有的情况再找外援
#         snippet.delete()
#         # 可以只返回状态码
#         return Response(status=status.HTTP_204_NO_CONTENT)


# 第一级开发方法结束，后面一级比一级高，一级比一级方便
# from django.shortcuts import render
#
# # Create your views here.
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer  # 将数据渲染成json格式
# from rest_framework.parsers import JSONParser  # 把从前端传过来的数据解析为json格式
# from snippetapp.models import Snippet
# from snippetapp.serializers import SnippetSerializer
#
#
# # list是五大接口之一
# # api的五大方式之一：列表
# @csrf_exempt  # 禁用跨域验证
# def snippet_list(request):
#     """
#     LC 列表、创建
#     """
#     if request.method == 'GET':
#         GET方法时，是外部请求数据，所以数据需要从数据库获取，自然就用模型的方法
#         snippets = Snippet.objects.all()
#         # 只要使用objects.all()，就需要many = True
#         serializer = SnippetSerializer(snippets, many=True)
#         # 这里serializer.data的数据是用来输出的，不需要验证
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# # api的五大方式之二：详情
# # 通常情况下：主键就是id（是因为将id设为主键了），但是主键是可以修改的
# # 主键必须是唯一的
# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     RUD 获取、更新、删除 Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)
#     # 实际使用中用PATCH
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         # 这里请求的数据要用，数据库里的数据也要用
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             # 更新成功，通知前端
#             return JsonResponse(serializer.data)
#         # 既然不符合，那么返回的就是序列器的错误，而不是返回原有的数据
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)
