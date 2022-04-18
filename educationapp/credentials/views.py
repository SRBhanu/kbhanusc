from pip._internal.network import auth
from pyexpat.errors import messages
from django.contrib import messages
from django.contrib import auth

from django.shortcuts import render, redirect

from django.contrib.auth.models import User


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['user_name']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request,"login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['Password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save() ;
                return redirect('login')

        else:
            messages.info(request, "password not matching")
        return redirect('register')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
