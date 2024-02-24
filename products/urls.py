from django.urls import path
from .views import *

urlpatterns = [
    path('', Prouducts, name='Prouducts'),
    path('add/', AddProduct, name='AddProduct'),
    path('delete/<int:id>/', DeleteProduct, name='DeleteProduct'),
    path('update/<int:id>/', UpdateProduct, name='UpdateProduct'),
]
