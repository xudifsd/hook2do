from django.conf.urls import patterns, include, url

from rest_framework.routers import DefaultRouter

from .views import ToDoItemListViewSet, ToDoItemViewSet

router = DefaultRouter()

router.register('todos', ToDoItemViewSet, base_name='todos')
router.register('lists', ToDoItemListViewSet, base_name='lists')

urlpatterns = patterns(
    '', 
    url(r'', include(router.urls)),
)
