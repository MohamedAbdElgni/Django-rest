from django.urls import path
from .views import *
urlpatterns = [
    path('', Cats, name='Cats'),
    path('add/', AddCat, name='AddCat'),
    path('update/<int:id>/', UpdateCat, name='UpdateCat'),
    path('delete/<int:id>/', DeleteCat, name='DeleteCat'),
]
