from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from authors.serializers import AuthorModelSerializer
from authors.models import Author
from todo.models import Project


# Create your views here.

class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

from rest_framework.response import Response

    
    
    



    