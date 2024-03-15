from django.urls import path
from .views import *

urlpatterns = [
    # path('autentication/', Registration.as_view(), name='autenticacion')
    path("signup/", SignUpView.as_view(), name="signup"),
]