from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout

from django.db import IntegrityError


def signup(request):
    if request.method == 'POST':
        if ' ' not in request.POST.get('name'):
            messages.info(request, 'Full name is incorrect!')
        elif request.POST.get('password') != request.POST.get('confirm-password'):
            messages.info(request, 'Passwords do not match!')

        else:
            user = User(
                first_name=request.POST.get('name').rsplit(' ')[0],
                last_name=request.POST.get('name').rsplit(' ')[1],
                username=request.POST.get('email'),
                email=request.POST.get('email'),
                password=make_password(request.POST.get('password'))
            )
            try:
                user.save()
                return redirect('login')
            except IntegrityError:
                messages.info(request, 'This user is already exist!')

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
            messages.info(request, 'Email or password is incorrect!')

    return render(request, 'login.html')


def logOut(request):
    logout(request)
    return redirect('login')


def account(request):
    return render(request, 'account.html', {'user': request.user})


def profile(request, id):
    user = User.objects.get(id=id)
    return render(request, 'profile.html', {'user': user})
