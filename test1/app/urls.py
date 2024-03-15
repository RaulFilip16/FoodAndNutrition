from django.urls import path
from .views import *

urlpatterns = [
    path('web/', get_barradenavegacion),
    path('students/', get_students),
    path('home/', home),
]