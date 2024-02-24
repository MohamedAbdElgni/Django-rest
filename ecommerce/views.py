from django.http import HttpResponse 
from django.shortcuts import render
from products.models import Product
from categories.models import Category
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

def Home(request):
    context = {
        'products':Product.objects.all(),
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:
            
            return render(request, 'registration/login.html', {'error_message': 'Invalid username or password.'})
    return render(request, 'registration/login.html')

def Logout(request):
    logout(request)
    return render(request, 'home.html')

def Register(request):
    
    return render(request, 'registration/registration.html')