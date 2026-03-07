from django.shortcuts import render , redirect

from .models import Task
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def task_list(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title,user=request.user)
        return redirect('task_list')

    

    query = request.GET.get('q')

    if query:
        tasks = Task.objects.filter(title__icontains=query)
    else:
        tasks = Task.objects.filter(user=request.user).order_by('-created')

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

def edit_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == "POST":
        title = request.POST.get('title')
        task.title = title
        task.save()
        return redirect('task_list')

    return render(request, 'edit_task.html', {'task': task})

def register(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        
        user = User.objects.create_user(username=username, password=password)
        login(request, user)

        return redirect('task_list')

    return render(request, 'tasks/register.html')

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('task_list')

    return render(request, 'tasks/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')