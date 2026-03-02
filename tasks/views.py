from django.shortcuts import render , redirect

from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def delete_task(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('task_list')