from django.urls import path
from .views import (
    task_list_view, task_create_view,
    task_toggle_status, task_delete
)

urlpatterns = [
    path('', task_list_view, name='task-list'),
    path('create/', task_create_view, name='task-create'),
    path('toggle/<int:task_id>/', task_toggle_status, name='task-toggle'),
    path('delete/<int:task_id>/', task_delete, name='task-delete'),
]
