from django.urls import path

from . import views
from .views import *

urlpatterns = [
    # path('students/', get_students),
    path('', home_noacc),
    path('home/', home),
    path('seleccionar-dia/',seleccionar_dia, name='seleccionar_dia'),

]