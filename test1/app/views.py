from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
import datetime as dt

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello world!")

def get_students(request):
    students = Student.objects.all()
    student_values = list(students.values())
    return JsonResponse(student_values, safe=False)

def get_website(request):
    return render(request, 'test.html')

def saludo(request):
    return HttpResponse("Hola como estas?")