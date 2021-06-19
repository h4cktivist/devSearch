from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout


def signup(request):
    if request.method == 'POST':
        user = User(
            first_name=request.POST.get('name').rsplit(' ')[0],
            last_name=request.POST.get('name').rsplit(' ')[1],
            username=request.POST.get('email'),
            email=request.POST.get('email'),
            password=make_password(request.POST.get('password'))
        )
        user.save()
        print(request.POST)
        return redirect('login')

    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('email'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    return render(request, 'login.html')


def logOut(request):
    logout(request)
    return redirect('login')
