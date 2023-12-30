from django.contrib import admin
from django.urls import path
from .views import homeView, schedulerView

urlpatterns = [
    path('', homeView, name='home'),
    path('scheduler/', schedulerView, name='scheduler'),
]