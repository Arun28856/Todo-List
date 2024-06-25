from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_complete=False).order_by('-updated_at')

    completed_task = Task.objects.filter(is_complete=True)
    print(completed_task)
    context = {
        'tasks': tasks,
        'completed_task': completed_task,
    }
    return render(request, 'home.html', context)