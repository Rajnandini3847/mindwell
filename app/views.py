from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

def bot(request):
    return render(request, 'bot.html')


def login_view(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  
        else:
            error_message = 'Invalid username or password.'

    return render(request, 'login.html', {'error_message': error_message})

def signup_view(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            error_message = 'Username already exists. Please choose a different one.'
        elif User.objects.filter(email=email).exists():
            error_message = 'Email already exists. Please use a different one.'
        else:
            User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')  

    return render(request, 'register.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('login')


