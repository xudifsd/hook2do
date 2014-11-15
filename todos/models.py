from django.db import models
from django.contrib.auth.models import User

TODO_ITEM_STATUS = (
    ('default', 'Default status'),
    ('scheduled', 'Scheduled status'),
    ('archived', 'archived status'),
)


class ToDoItemList(models.Model):

    """List to organize todo items """
    name = models.CharField(max_length=64, unique=True)
    is_archived = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    owner = models.ForeignKey(User, related_name='lists')


class ToDoItem(models.Model):

    """To do items' model"""

    content = models.CharField(max_length=256)
    itemlist = models.ForeignKey(ToDoItemList, related_name='todos', null=True, blank=True)
    status = models.CharField(max_length=16, choices=TODO_ITEM_STATUS, default='default')

    due_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    owner = models.ForeignKey(User, related_name='todos')


class TimeLogEntry(models.Model):

    """Each entry represents the user is working on the corresponding task during the period."""

    todoItem = models.ForeignKey(ToDoItem, related_name="logs")
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(null=True, blank=True)