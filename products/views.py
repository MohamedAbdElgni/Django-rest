from .models import Product 
from django.views.generic import ListView , CreateView, UpdateView, DeleteView
from .forms import *
from django.urls import reverse_lazy


# Create your views here.

class ProuductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    

class AddProduct(CreateView):
    model = Product
    template_name = 'products/add_product.html'
    Form_class = 'form'
    fields = ['name', 'price', 'description', 'img', 'category']
    success_url = reverse_lazy('Prouducts')
    

class UpdateProduct(UpdateView):
    model = Product
    template_name = 'products/update_prod.html'
    Form_class = 'form'
    fields = ['name', 'price', 'description', 'img', 'category']
    success_url = reverse_lazy('Prouducts')
    

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'products/delete_prouduct.html'
    success_url = reverse_lazy('Prouducts')
    
    