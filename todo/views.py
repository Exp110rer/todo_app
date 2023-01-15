from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from todo.models import Project, todo
from todo.serializers import ProjectSerializer, todoSerializer

# Create your views here.

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class todoViewSet(ModelViewSet):
    queryset = todo.objects.all()
    serializer_class = todoSerializer