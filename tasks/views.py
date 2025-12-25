from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return tasks only for logged-in user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign task to logged-in user
        serializer.save(user=self.request.user)
