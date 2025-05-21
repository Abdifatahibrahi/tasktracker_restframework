from rest_framework import generics, filters
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated  # <-- Add this import

# For the API views:
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date', 'priority']
    permission_classes = [IsAuthenticated]  # <-- Add this line

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # <-- Add this line

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)

# For the template view:
@login_required
def task_list_view(request):
    return render(request, 'tasks/task_list.html')