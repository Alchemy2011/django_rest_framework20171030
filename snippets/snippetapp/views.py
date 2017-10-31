from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from snippetapp.models import Snippet
from snippetapp.serializers import SnippetSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
