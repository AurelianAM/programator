from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import MyUserCreationForm, MyUserLoginForm

# Create your views here.


def loginView(request):
    if request.method == "GET":
        form = MyUserLoginForm()
        return render(request, 'login.html', {"form": form})
    if request.method == "POST":
        form = MyUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')
                return render(request, 'login.html', {"form": form})
        else:
            return render(request, 'login.html', {"form": form})

def logoutView(request):
    logout(request)
    return redirect('home')

def registerView(request):
    if request.method == "GET":
        form = MyUserCreationForm()
        return render(request, 'register.html', {"form": form})
    
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'register.html', {"form": form})

        