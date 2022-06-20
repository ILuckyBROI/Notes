from django.urls import path
from .views import UserCustomViewSet

app_name = 'TODO'
urlpatterns = [
    path('', UserCustomViewSet.as_view({'get': 'list'})),
]
