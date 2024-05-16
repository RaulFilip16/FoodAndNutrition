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


from datetime import datetime, timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Dish
from .forms import DishForm

def seleccionar_dia(request):
    date_param = request.GET.get('date')

    if date_param:
        try:
            current_date = datetime.strptime(date_param, '%B %d, %Y').date()
        except ValueError:
            current_date = datetime.strptime(date_param, '%Y-%m-%d').date()
    else:
        current_date = datetime.now().date()

    previous_date = current_date - timedelta(days=1)
    next_date = current_date + timedelta(days=1)
    platos = Dish.objects.filter(date=current_date)

    add_form = DishForm()
    modify_form = DishForm()

    if request.method == 'POST':
        if 'plato_id' in request.POST:
            plato_id = request.POST.get('plato_id')
            plato = get_object_or_404(Dish, id=plato_id)

            if 'delete' in request.POST:
                plato.delete()
                return redirect(reverse('seleccionar_dia') + f'?date={current_date.strftime("%B %d, %Y")}')
            elif 'modify' in request.POST:
                modify_form = DishForm(request.POST, instance=plato)
                if modify_form.is_valid():
                    modify_form.save()
                    return redirect(reverse('seleccionar_dia') + f'?date={current_date.strftime("%B %d, %Y")}')
        else:
            add_form = DishForm(request.POST)
            if add_form.is_valid():
                add_form.instance.date = current_date
                add_form.save()
                return redirect(reverse('seleccionar_dia') + f'?date={current_date.strftime("%B %d, %Y")}')

    return render(request, 'seleccionar_dia.html', {
        'add_form': add_form,
        'modify_form': modify_form,
        'current_date': current_date,
        'previous_date': previous_date,
        'next_date': next_date,
        'platos': platos,
    })