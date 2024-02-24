from django.http import HttpResponse 
from django.shortcuts import render
from products.models import Product
from categories.models import Category

def Home(request):
    context = {
        'products':Product.get_all_products()
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def Login(request):
    return render(request, 'login.html')

def Register(request):
    return render(request, 'register.html')

def Logout(request):
    pass