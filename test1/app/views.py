from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.

# def get_students(request):
#     students = Student.objects.all()
#     student_values = list(students.values())
#     return JsonResponse(student_values, safe=False)

def home(request):
    return render(request, 'home/home.html', name = 'home')

