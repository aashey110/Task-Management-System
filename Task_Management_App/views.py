from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status
from .models import CustomUser
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        user = CustomUser.objects.create_user(username=username, password=password, role=role)
        if user is not None:
            user.save()
            messages.success(request, "Registration successful!")

            return redirect('signup')
    return render(request, 'signup.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.role == 'admin':
                login(request, user)
                return redirect('admin_home')
            elif user.role == 'user':
                login(request, user)
                return redirect('user_home')
    return render(request, 'user_login.html')


def user_logout(request):
    logout(request)
    return redirect('user_login')
    

def user_home(request):
    return render(request, 'user_home.html')


def admin_home(request):
    return render(request, 'admin_home.html')


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def task_api(request, pk=None):
#     if request.method == 'GET':
#         id = pk
#         if id is not None:
#             task = Task.objects.get(id=id)
#             serializer = TaskSerializer(task)
#             return Response(serializer.data)
#         task = Task.objects.all()
#         serializer = TaskSerializer(task, many = True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Task Added'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PUT':
#         id = pk
#         task = Task.objects.get(id=id)
#         serializer = TaskSerializer(task, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Task Updated'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PATCH':
#         id = pk
#         task = Task.objects.get(id=id)
#         serializer = TaskSerializer(task, data = request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Task Partially Updated'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == "DELETE":
#         id = pk
#         task = Task.objects.get(id=id)
#         task.delete()
#         return Response({'msg': 'Task Deleted'}, status=status.HTTP_200_OK)
    


    
def add_task(request):

    show_user = CustomUser.objects.all()

    if request.method == 'POST':
        task_name = request.POST.get('title')
        task_description = request.POST.get('description')
        task_status = request.POST.get('status')
        task_duedate = request.POST.get('due_date')
        task_assign_to = request.POST.get('assign_to')

        Task.objects.create(title=task_name, description=task_description, status=task_status, due_date=task_duedate, assignto_id=task_assign_to)
        messages.success(request, "Task has been added successfully!")

        return redirect('add_task')
    return render(request, 'add_task.html', {"user_list": show_user})

def show_task(request):
    task_list = Task.objects.all()
    return render(request, 'show_task.html', {"task_list": task_list})

