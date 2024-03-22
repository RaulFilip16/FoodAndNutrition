from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# Create your views here.

def authentication(request):
    return render(request, 'autentication.html')

def home(request):
    return render(request, 'home/home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "User are already registrated. Please try again or log in with your account!")
            return redirect('home')
        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, '¡Succesful registration!')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

        return redirect('home')
       
    return render(request, 'signup.html')