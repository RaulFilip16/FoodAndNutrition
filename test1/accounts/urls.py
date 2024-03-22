from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('authentication/', authenticate, name='autentication'),
    path('signup/', signup, name='signup'),
    path('home/',home, name='home'),
]