from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User, Project, Todo


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProjectModelSerializer(HyperlinkedModelSerializer):
    users = UserModelSerializer(many=True)
    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
