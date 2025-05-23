
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, task_list_view
from django.urls import path, include

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('home/', task_list_view, name='task-list')

]