from django.shortcuts import render, redirect
from django.contrib import auth

from .forms import UserLoginForm, UserRegistrationForm
from .models import User



def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('BlogPost:index')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request,'users/login.html', context)

def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request,'users/registration.html', context)


def logout(request):
    auth.logout(request)
    return redirect('BlogPost:index')

# Create your views here.
