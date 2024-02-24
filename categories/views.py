from .models import Category 
from django.views.generic import ListView , CreateView, UpdateView, DeleteView
from .forms import *
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.

class CategoryListView(ListView):
    model = Category
    template_name = 'categories/cats.html'
    context_object_name = 'cats'
    
@method_decorator(login_required, name='dispatch')
class AddCategory(CreateView):
    model = Category
    template_name = 'categories/add_cat.html'
    Form_class = 'form'
    fields = ['name', 'description', 'img']
    success_url = reverse_lazy('Cats')
    
@method_decorator(login_required, name='dispatch')
class UpdateCategory(UpdateView):
    model = Category
    template_name = 'categories/update_cat.html'
    Form_class = 'form'
    fields = ['name', 'description', 'img']
    success_url = reverse_lazy('Cats')
    
@method_decorator(login_required, name='dispatch')  
class DeleteCategory(DeleteView):
    model = Category
    template_name = 'categories/delete_cat.html'
    success_url = reverse_lazy('Cats')