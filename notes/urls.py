from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mainapp.views import AuthorModelViewSet, BiographyModelViewSet, BookModelViewSet, ArticleModelViewSet, MyAPIView
from TODO.views import UserCustomViewSet, ProjectModelViewSet, TodoModelViewSet

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('biographies', BiographyModelViewSet)
router.register('articles', BookModelViewSet)
router.register('books', ArticleModelViewSet)

router.register('user', UserCustomViewSet)
router.register('project', ProjectModelViewSet)
router.register('todo', TodoModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('myapi/', MyAPIView.as_view()),
]
