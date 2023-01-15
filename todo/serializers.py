from rest_framework.serializers import ModelSerializer, StringRelatedField, HyperlinkedModelSerializer
from todo.models import Project, todo

class ProjectSerializer(HyperlinkedModelSerializer):
    user = StringRelatedField(many = True)
    class Meta:
        model = Project
        fields = '__all__'


class SingleProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        exclude = ('id', )


class todoSerializer(ModelSerializer):
    project = SingleProjectSerializer()
    class Meta:
        model = todo
        exclude = ('id',)

