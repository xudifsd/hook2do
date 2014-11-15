from rest_framework import viewsets

from .serializers import ToDoItemListSerializer, ToDoItemSerializer

class ToDoItemListViewSet(viewsets.ModelViewSet):

    """API viewsets to retrieve and modify ToDoItemList"""
    serializer_class = ToDoItemListSerializer

    def get_queryset(self):
        return self.request.user.lists.all()

    def pre_save(self, obj):
        obj.owner = self.request.user


class ToDoItemViewSet(viewsets.ModelViewSet):

    """API viewsets to retrieve and modify ToDoItem"""
    serializer_class = ToDoItemSerializer

    def get_queryset(self):
        return self.request.user.todos.all()

    def pre_save(self, obj):
        obj.owner = self.request.user
