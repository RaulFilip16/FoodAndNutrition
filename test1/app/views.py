from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

def get_students(request):
    students = Student.objects.all()
    student_values = list(students.values())
    return JsonResponse(student_values, safe=False)

def get_website(request):
    return render(request, 'test.html')


def home(request):
    return render(request, 'home.html')