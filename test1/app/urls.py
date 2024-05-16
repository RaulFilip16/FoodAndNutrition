from django.urls import path

from . import views
from .views import *


urlpatterns = [
    # path('students/', get_students),
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('aboutUs/', aboutUs, name='aboutUs'),
    path('contacto/', contacto, name='contacto'),
    path('seleccionar-dia/', seleccionar_dia, name='seleccionar_dia'),

]