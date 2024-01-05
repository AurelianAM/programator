from django.contrib import admin
from django.urls import path
from .views import loginView, logoutView, registerView

urlpatterns = [
    path('login/', loginView, name='myLogin'),
    path('logout/', logoutView, name='myLogout'),
    path('register/', registerView, name='myRegister'),
]