from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def aut(request):
    return render(request, 'autentication.html')

class Registration(View):
    # el metodo GET sirve para mostrarnos el formulario, i SE ESTA mostrando  
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/login.html', {"form":form}) 
    
    # el metodo POST es el que gestiona el envio de informacion a traves del formulario, ES DECIR el usuario y la contraseña
    def post(self, request):
        form = UserCreationForm(request.POST)
        # if form.is_valid():
        user = form.save()
        login(request, user)
        return reverse_lazy('home.html')
    

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login") # Redirect to the login page after a successful registration
    template_name = "registration/signup.html" # The template used to render the page