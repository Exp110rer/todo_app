from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from authapp.serializers import PortalUserModelSerializer
from authapp.models import PortalUser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

# Create your views here.

class PortaUserModelViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = PortalUser.objects.all()
    serializer_class = PortalUserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
