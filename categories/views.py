from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .forms import CategoryForm, UpdateCategory
from .models import Category
# Create your views here.



def Cats (request):
    context = {
        'cats':Category.get_all_categories()
    }
    return render(request, 'categories/cats.html', context)

def AddCat(request):
    form = CategoryForm()
    context={
        'form':form,
        "msg":{
            "txt":"",
            "type":""
        }
    }
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)  
        if form.is_valid():
            cat = Category()
            cat.name = form.cleaned_data['name']
            cat.description = form.cleaned_data['description']
            if 'img' in request.FILES:
                cat.img = request.FILES['img']
            cat.save()
            context['msg']['txt'] = "Category added successfully"
            context['msg']['type'] = "success"
            return HttpResponseRedirect(reverse('Cats') ,context['msg'])
        else:
            print(form.errors)
            context['form'] = form
            context['msg']['txt'] = form.errors
            context['msg']['type'] = "danger"
    return render(request, 'categories/add_cat.html', context)




def UpdateCat(response,id):
    cat = Category.objects.get(id=id)
    form = UpdateCategory()
    form.fields['name'].initial = cat.name
    form.fields['description'].initial = cat.description
    form.fields['img'].initial = cat.img
    context = {
        'cat':cat,
        'form':form,
        "msg":{
            "txt":"",
            "type":""
        }
    }
    
    if response.method == 'POST':
        form = UpdateCategory(response.POST, response.FILES)
        if form.is_valid():
            cat.name = form.cleaned_data['name']
            cat.description = form.cleaned_data['description']
            if 'img' in response.FILES:
                cat.img = response.FILES['img']
            cat.save()
            context['msg']['txt'] = "Category updated successfully"
            context['msg']['type'] = "success"
            return HttpResponseRedirect(reverse('Cats') ,context['msg'])
        else:
            context['form'] = form
            context['msg']['txt'] = form.errors
            context['msg']['type'] = "danger"
    return render(response, 'categories/update_cat.html', context)


def DeleteCat(response, id):
    cat = Category.objects.get(id=id)
    cat.delete()
    return HttpResponseRedirect(reverse('Cats'))