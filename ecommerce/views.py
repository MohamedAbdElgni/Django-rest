
from django.shortcuts import render,reverse,redirect
from django.http import HttpResponseRedirect
from products.models import Product
from django.contrib.auth import authenticate, login,logout, get_user_model

from .forms import SignupForm , LoginForm




def Home(request):
    context = {
        'products':Product.objects.all(),
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def Login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('Home'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('Home'))
            else:
                print('Invalid Username or Password')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})





def Register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('Home'))
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Login'))
        
        else:
            for error in list(form.errors.values()):
                print(request,error)
    else:
        form = SignupForm()
    return render(request, 'registration/registration.html', {'form': form})

def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home'))