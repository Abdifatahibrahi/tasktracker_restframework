from django.contrib import admin
from django.urls import path, include
from tasks.views import TaskListCreateView, TaskRetrieveUpdateDestroyView, task_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),
    path('', task_list_view, name='task-list'),
]