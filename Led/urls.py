from django.urls import path
from . import views

urlpatterns = [
    path('prueba/', views.prueba, name='prueba'),
    path('control_led/', views.control_led, name='control_led'),
]
