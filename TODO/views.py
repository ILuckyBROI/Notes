from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import mixins, viewsets
from .models import User, Project, Todo
from .serializers import UserModelSerializer, ProjectModelSerializer, TodoModelSerializer
from .filters import ProjectFilter, TodoFilter


class UserCustomViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class ProjectPaginator(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    pagination_class = ProjectPaginator


class TodoPaginator(LimitOffsetPagination):
    default_limit = 20


class TodoModelViewSet(ModelViewSet):
    def perform_destroy(self, instance):
        closed = Todo.status.STATUS_CLOSED
        instance.save(closed)

    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    filterset_class = TodoFilter
    pagination_class = TodoPaginator
