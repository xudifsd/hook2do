from rest_framework import serializers

from .models import ToDoItemList, ToDoItem

class ToDoItemListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoItemList
        exclude = ('owner', )


class ToDoItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoItem
        exclude = ('owner', )
