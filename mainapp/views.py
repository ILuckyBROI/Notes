from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Author, Biography, Book, Article
from .serializers import AuthorModelSerializer, BiographyModelSerializer, BookModelSerializer, ArticleModelSerializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class MyAPIView(APIView):
    # class MyAPIView(CreateAPIView, ListAPIView):
    # APIView
    def get(self, request):
        return Response({'date': 'GET SUCCESS'})

    def post(self, request):
        return Response({'date': 'POST SUCCESS'})

    renderer_classes = [JSONRenderer]
    # queryset = Author.object.all()
    # serializer_class = AuthorModelSerializer
