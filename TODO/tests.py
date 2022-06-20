import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from django.contrib.auth.models import User as Admins
from .views import UserCustomViewSet, ProjectModelViewSet
from .models import User, Project, Todo


class TestUserCustomViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/user')
        view = UserCustomViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/project/', {'title': 'alr85ece-2d73-4e84-9392-596f5d2d2e28',
                                                 'project_url': 'http://karamel.com',
                                                 'users': 'Mash'})
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/project/', {'title': 'alr85ece-2d73-4e84-9392-596f5d2d2e28',
                                                 'project_url': 'http://karamel.com',
                                                 'users': 'Mash'})
        admin = Admins.objects.create_superuser('admin', 'min@ada.com', 'admin')
        force_authenticate(request, admin)
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        user = User.objects.create(uid='2b185ece-2d73-4e84-9392-596f5d2d2e01',
                                   username='Pok',
                                   first_name='Mana',
                                   last_name='Looni',
                                   password='Comkonikoasdf1sdf5',
                                   email='Malonii@bruh.com')
        client = APIClient()
        response = client.get(f'/api/user/{user.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        user = User.objects.create(uid='2b185ece-2d73-4e84-9392-596f5d2d2e01',
                                   username='Pok',
                                   first_name='Mana',
                                   last_name='Looni',
                                   password='Comkonikoasdf1sdf5',
                                   email='Malonii@bruh.com')
        client = APIClient()
        admin = Admins.objects.create_superuser('admin', 'min@ada.com', 'admin')
        client.login(username='admin', password='admin')
        response = client.put(f'/api/user/{user.uid}/',
                              {'username': 'Mono', 'first_name': 'Last', 'last_name': 'Marine', })
        user = User.objects.get(pk=user.uid)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(user.username, 'Mono')


class TestUserViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/user/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
