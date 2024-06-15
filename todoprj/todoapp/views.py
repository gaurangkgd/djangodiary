from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = todo(user=request.user, todo_name=task)
        new_todo.save()

    all_todos = todo.objects.filter(user=request.user)
    context = {
        'todos': all_todos
    }
    return render(request, 'todoapp/todo.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 3:
            messages.error(request, 'Password must be at least 3 characters')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Error, username already exists, use another.')
            return redirect('register')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()

        messages.success(request, 'User successfully created, login now')
        return redirect('login')
    return render(request, 'todoapp/register.html', {})

def LogoutView(request):
    logout(request)
    return redirect('login')

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.error(request, 'Error, wrong user details or user does not exist')
            return redirect('login')

    return render(request, 'todoapp/login.html', {})

@login_required
def DeleteTask(request, id):
    try:
        get_todo = todo.objects.get(user=request.user, id=id)
        get_todo.delete()
    except todo.DoesNotExist:
        messages.error(request, 'Todo item does not exist.')
    return redirect('home-page')

@login_required
def Update(request, id):
    try:
        get_todo = todo.objects.get(user=request.user, id=id)
        get_todo.status = True
        get_todo.save()
    except todo.DoesNotExist:
        messages.error(request, 'Todo item does not exist.')
    return redirect('home-page')
@login_required
def edit_task(request, id):
    todo_item = get_object_or_404(todo, id=id, user=request.user)

    if request.method == 'POST':
        new_task = request.POST.get('task')
        todo_item.todo_name = new_task
        todo_item.save()
        messages.success(request, 'Task updated successfully!')
        return redirect('home-page')

    context = {
        'todo_item': todo_item
    }
    return render(request, 'todoapp/edit_task.html', context)
