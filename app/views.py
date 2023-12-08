from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .bot import call_bot
from django.http import JsonResponse
from .models import *
from .intent_ana import *
# Create your views here.

def bot(request):
    if request.method == 'POST':
        try:
            # Get the user input from the request data
            user_input = request.POST.get('user_input', '')
            response = call_bot(user_input)
            
            # Save the chat history
            Chat.objects.create(user_input=user_input, response=response)

            chat_history = Chat.objects.all().order_by('-timestamp')
            return render(request, 'bot.html', {'chat_history': chat_history})
        except Exception as e:
            return render(request, 'bot.html', {'error': str(e)})

    # Retrieve all chat history
    chat_history = Chat.objects.all().order_by('-timestamp')
    return render(request, 'bot.html', {'chat_history': chat_history})


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

    return render(request, 'signup.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('login')

def analyse_intent(request):
    if request.method == 'POST':
        try:
            # Get the user input from the request data
            user_input = request.POST.get('user_input', '')
            response = main_function(user_input)
            
            return render(request, 'intent.html',{'response': response})
        except Exception as e:
            return render(request, 'intent.html', {'error': str(e)})
    return render(request, 'intent.html')


from django.shortcuts import render
from django.http import HttpResponse
from .models import SadSongs, HappySongs, CalmSongs

def listen_music(request):
    try:
        user_input = Chat.objects.latest('-timestamp').user_input
        response = main_function(user_input)

        if response == 'relationship-b':
            songs = SadSongs.objects.all()
        elif response == 'happy':
            songs = HappySongs.objects.all()
        elif response == 'calm':
            songs = CalmSongs.objects.all()
        else:
            songs = SadSongs.objects.all()

        # Render the HTML content
        return render(request, 'music.html', {'songs': songs})

    except Exception as e:
        error_message = str(e)
        return render(request, 'error.html', {'error': error_message})



