from django.shortcuts import render, redirect
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














# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout 
# from django.contrib import messages
# from .models import todo

# # Create your views here.

# def home(request):
#     if request.method == 'POST':
#         task = request.POST.get('task')
#         new_todo = todo(user=request.user, todo_name=task)
#         new_todo.save()

#     all_todos = todo.objects.filter(user=request.user)
#     context = {
#         'todos': all_todos
#     }
#     return render(request, 'todoapp/todo.html', context)

# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         if len(password) < 3:
#             messages.error(request, 'Password must be at least 3 characters')
#             return redirect('register')
        
#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Error, username already exists. Use another.')
#             return redirect('register')

#         new_user = User.objects.create_user(username=username, email=email, password=password)
#         new_user.save()
#         messages.success(request, 'User successfully created, login now')
#         return redirect('login')
#     return render(request, 'todoapp/register.html', {})

# def loginpage(request):
#     if request.method == 'POST':
#         username = request.POST.get('uname')
#         password = request.POST.get('pass')

#         validate_user = authenticate(username=username, password=password)
#         if validate_user is not None:
#             login(request, validate_user)
#             return redirect('home-page')
#         else:
#             messages.error(request, 'Error, wrong user details or user does not exist.')
#             return redirect('login')

#     return render(request, 'todoapp/login.html', {})

# def DeleteTask(request, name):
#     # Use get_object_or_404 to handle non-existent objects gracefully
#     get_todo = get_object_or_404(todo, user=request.user, todo_name=name)
#     get_todo.delete()
#     return redirect('home-page')

# def Update(request, name):
#     # Placeholder for the update view logic
#     pass
