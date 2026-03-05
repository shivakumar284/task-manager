from django.shortcuts import render , redirect

from .models import Task

def task_list(request):
    if request.method == "POST":
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list')

    tasks = Task.objects.all().order_by('-created')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def delete_task(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('task_list')

def toggle_complete(request, id):
    task = Task.objects.get(id=id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')