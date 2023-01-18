from rest_framework.serializers import ModelSerializer, ModelSerializer
from authors.models import Author

class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'