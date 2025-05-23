from rest_framework import generics, filters
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated  # <-- Add this import
from rest_framework import viewsets, permissions
from .serializers import *
from .models import Task
from rest_framework import filters

class TaskViewSet(viewsets.ModelViewSet):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['created_at',]
    search_fields = ['title', 'description', 'status']

    def get_queryset(self):
        return super().get_queryset()
    
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)


# For the template view:
@login_required
def task_list_view(request):
    return render(request, 'tasks/task_list.html')