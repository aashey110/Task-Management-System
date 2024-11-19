from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser

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
            return redirect('signup')
    return render(request, 'signup.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_home')
    return render(request, 'user_login.html')


def user_logout(request):
    logout(request)
    return redirect('user_login')
    

def user_home(request):
    return render(request, 'user_home.html')