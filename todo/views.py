from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from todo.models import Project, todo
from todo.serializers import ProjectSerializer, todoSerializer


# Create your views here.

# class ProjectViewSet(ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

class ProjectModelPageNumberPagination(PageNumberPagination):
    page_size = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectModelPageNumberPagination
    filterset_fields = ['name']


class todoViewSet(ModelViewSet):
    queryset = todo.objects.all()
    serializer_class = todoSerializer