from django.urls import path
from .views import *

urlpatterns = [
    path('', ProuductsListView.as_view(), name='Prouducts'),
    path('add/', AddProduct.as_view(), name='AddProduct'),
    path('update/<int:pk>/', UpdateProduct.as_view(), name='EditProduct'),
    path('delete/<int:pk>/', DeleteProduct.as_view(), name='DeleteProduct'),
    # path('add/', AddProduct, name='AddProduct'),
    # path('delete/<int:id>/', DeleteProduct, name='DeleteProduct'),
    # path('update/<int:id>/', UpdateProduct, name='UpdateProduct'),
]
