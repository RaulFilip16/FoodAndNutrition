from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import CreateView

from .models import *
from .forms import DishForm


# Create your views here.

# def get_students(request):
#     students = Student.objects.all()
#     student_values = list(students.values())
#     return JsonResponse(student_values, safe=False)

def home(request):  # cuan ya esta fet login o singup
    return render(request, 'home/home.html', name='home')


def home_noacc(request):
    return render(request, 'menu.html')


def seleccionar_dia(request):
    # Obtenemos la fecha actual o la fecha proporcionada en la consulta
    if 'date' in request.GET:
        current_date = datetime.strptime(request.GET['date'], '%Y-%m-%d').date()
    else:
        current_date = datetime.now().date()

    # Calculamos las fechas anterior y siguiente
    previous_date = current_date - timedelta(days=1)
    next_date = current_date + timedelta(days=1)

    # Filtramos los platos por la fecha actual
    platos = Dish.objects.filter(date=current_date)

    # Si el método de la solicitud es POST, procesamos el formulario
    if request.method == 'POST':
        form = DishForm(request.POST)
        # Si el formulario es válido, guardamos el nuevo Dish
        if form.is_valid():
            form.save()
            # Redirigimos al usuario de nuevo a la misma página
            return redirect('seleccionar_dia')
    else:
        # Si la solicitud no es POST, creamos una instancia del formulario
        form = DishForm()

    # Renderizamos el template con el formulario, las fechas y los platos
    return render(request, 'seleccionar_dia.html', {
        'form': form,
        'current_date': current_date,
        'previous_date': previous_date,
        'next_date': next_date,
        'platos': platos,  # Pasamos los platos al template
    })