from django.contrib import admin
from django.urls import path
from .views import homeView, schedulerView, mediciView

urlpatterns = [
    path('', homeView, name='home'),
    path('scheduler/', schedulerView, name='scheduler'),
    path('medici/', mediciView, name='medici'),
]