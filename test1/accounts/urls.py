from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('authentication/', authentication, name='autentication'),
    path('signup/', signup, name='signup'),
    path('home/',home, name='home'),
    path('login/', logIn, name='login'),
    path('logout/', logOut, name='logout')

]