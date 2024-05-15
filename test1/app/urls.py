from django.urls import path

from . import views
from .views import *

urlpatterns = [
    # path('students/', get_students),
    path('', home_noacc),
    path('home/', home),
    path('seleccionar-dia/',seleccionar_dia, name='seleccionar_dia'),
    path('eliminar-plato/<int:plato_id>/',eliminar_plato, name='eliminar_plato'),
    path('modificar-plato/<int:plato_id>/', views.modificar_plato, name='modificar_plato'),

]