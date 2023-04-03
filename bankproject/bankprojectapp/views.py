from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate


# Create your views here.
def index(request):
    return render(request, "home.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username is exist ")
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, password1=password1, password2=password2)
                user.save();
                messages.info(request, "registered ")
                return redirect('login')

        else:
            messages.info(request, "password is incorrect")
            return redirect('/register')
    return render(request, "register.html")
    #
    # return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'username or password not correct')
            return redirect('register')
        else:
            return redirect('/login')
    return render(request, "login.html")


def formpage(request):

    if request.method == 'POST':
        username = request.POST['username']
        email=request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.info(request,"username taken")
            return redirect('/formpage')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email taken")
            return redirect('/formpage')
        else:
            user=User.objects.create_user(username=username,email=email)
            user.save();
            messages.info(request,"application accepted")
            return redirect('/')

    return render(request, 'formpage.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
