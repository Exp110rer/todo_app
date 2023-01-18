from rest_framework.serializers import ModelSerializer
from authapp.models import PortalUser

class PortalUserModelSerializer(ModelSerializer):
    class Meta:
        model = PortalUser
        exclude = ('password',)
