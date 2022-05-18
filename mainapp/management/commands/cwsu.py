from typing import List

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from mainapp.models import Author


class Command(BaseCommand):
    help = 'Used to create a superuser and three users'

    def handle(self, *args, **options):
        user_name = ['Admiral', 'General', 'Marine']
        first_name = ['Vasya', 'Kirill', 'Albert']
        last_name = ['Bochkov', 'Shalkov', 'Mafioznik']
        email = ['Shovel@wolf.com', 'Shavel@wolf.com', 'Mafi@wolf.com']
        password = ['Admiralnu', 'Generaltop', '123Marine321']
        User.objects.create_superuser(username='Total', password='Total')
        for i in range(3):
            User.objects.create_user(username=user_name[i], first_name=first_name[i], last_name=last_name[i],
                                     email=email[i], password=password[i])
