from django.urls import path
from .views import (Login_form, Login_success, register)

urlpatterns =[
    path('login/',Login_form,name='login'),
    path('registeration/',register,name="register"),
    path('success/',Login_success,name='success'),
]
