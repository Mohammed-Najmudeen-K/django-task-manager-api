from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from django.core.paginator import Paginator

# ---------------- API VIEWS ----------------
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# ---------------- TEMPLATE VIEWS ----------------
@login_required
def task_list_view(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(tasks, 5)  # 5 tasks per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'tasks/task_list.html', {'page_obj': page_obj})

@login_required
def task_create_view(request):
    if request.method == 'POST':
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST.get('description', ''),
            user=request.user
        )
        return redirect('task-list')
    return render(request, 'tasks/task_form.html')

@login_required
def task_toggle_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task-list')

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('task-list')
