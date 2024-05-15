from datetime import datetime, timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
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
    if 'date' in request.GET:
        current_date = datetime.strptime(request.GET['date'], '%Y-%m-%d').date()
    else:
        current_date = datetime.now().date()
    previous_date = current_date - timedelta(days=1)
    next_date = current_date + timedelta(days=1)
    platos = Dish.objects.filter(date=current_date)

    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.instance.date = current_date
            form.save()
            return redirect(reverse('seleccionar_dia') + f'?date={current_date}')
    else:
        form = DishForm()

    return render(request, 'seleccionar_dia.html', {
        'form': form,
        'current_date': current_date,
        'previous_date': previous_date,
        'next_date': next_date,
        'platos': platos,
    })
def eliminar_plato(request, plato_id):
    plato = get_object_or_404(Dish, id=plato_id)
    if request.method == 'POST':
        plato.delete()
        return redirect(reverse('seleccionar_dia') + f'?date={plato.date}')
    return render(request, 'eliminar_plato.html', {'plato': plato})


def modificar_plato(request, plato_id):
    plato = get_object_or_404(Dish, id=plato_id)
    if request.method == 'POST':
        form = DishForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect(reverse('seleccionar_dia') + f'?date={plato.date}')
    else:
        form = DishForm(instance=plato)

    return render(request, 'modificar_plato.html', {'form': form, 'plato': plato})