from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class User(User):
    uid = models.UUIDField(primary_key=True, default=uuid4())


class Project(models.Model):
    title = models.CharField(max_length=64)
    project_url = models.URLField()
    users = models.ManyToManyField(User)


class Todo(models.Model):
    STATUS_OPEN = '1'
    STATUS_CLOSED = '2'
    CHOOSING_STATUS = ((STATUS_OPEN, 'open'), (STATUS_CLOSED, 'close'))
    project = models.ForeignKey(Project, models.CASCADE)
    text = models.CharField(max_length=64)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(User)
    status = models.CharField(max_length=5, choices=CHOOSING_STATUS, default=STATUS_OPEN)
