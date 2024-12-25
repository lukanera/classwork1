from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout, authenticate

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    R_or_L = ['register']
    form = UserRegisterForm()
    return render(request, 'user_form.html', {'form': form, 'R_or_L': R_or_L})

def login_view(request):
    form = UserLoginForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'user_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login_view')