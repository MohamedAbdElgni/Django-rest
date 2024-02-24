from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from categories.models import Category
from .forms import *


# Create your views here.

def Prouducts(request):
    context = {
        'products':Product.get_all_products()
    }
    return render(request, 'products/products.html', context)


def AddProduct(request):
    form = AddProductForm()
    context={
        'form':form,
        "msg":{
            "txt":"",
            "type":""
        }
    }
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)  
        if form.is_valid():
            prod = Product()
            prod.name = form.cleaned_data['name']
            prod.description = form.cleaned_data['description']
            prod.price = form.cleaned_data['price']
            prod.category = Category.objects.get(id=form.cleaned_data['category'].id)
            if 'img' in request.FILES:
                prod.img = request.FILES['img']
            prod.save()
            context['msg']['txt'] = "Product added successfully"
            context['msg']['type'] = "success"
        else:
            print(form.errors)
            context['form'] = form
            context['msg']['txt'] = form.errors
            context['msg']['type'] = "danger"
    return render(request, 'products/add_product.html', context)

def DeleteProduct(request, id):
    Product.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('Prouducts'))


def UpdateProduct(response,id):
    prod = Product.objects.get(id=id)
    form = UpdateProductForm()
    form.fields['name'].initial = prod.name
    form.fields['description'].initial = prod.description
    form.fields['price'].initial = prod.price
    form.fields['category'].initial = prod.category
    form.fields['img'].initial = prod.img
    context = {
        'prod':prod,
        'form':form,
        "msg":{
            "txt":"",
            "type":""
        }
    }
    if response.method == 'POST':
        form = UpdateProductForm(response.POST, response.FILES)
        if form.is_valid():
            prod.name = form.cleaned_data['name']
            prod.description = form.cleaned_data['description']
            prod.price = form.cleaned_data['price']
            prod.category = Category.objects.get(id=form.cleaned_data['category'].id)
            if 'img' in response.FILES:
                prod.img = response.FILES['img']
            prod.save()
            context['msg']['txt'] = "Product updated successfully"
            context['msg']['type'] = "success"
            return HttpResponseRedirect(reverse('Prouducts') ,context['msg'])
        else:
            print(form.errors)
            context['form'] = form
            context['msg']['txt'] = form.errors
            context['msg']['type'] = "danger"
    return render(response, 'products/update_prod.html', context)
