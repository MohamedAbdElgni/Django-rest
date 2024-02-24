from django.urls import path
from .views import *
urlpatterns = [
    path('', CategoryListView.as_view(), name='Cats'),
    path('add/', AddCategory.as_view(), name='AddCat'),
    path('update/<int:pk>/', UpdateCategory.as_view(), name='UpdateCat'),
    path('delete/<int:pk>/', DeleteCategory.as_view(), name='DeleteCat'),
    # path('add/', AddCategory, name='AddCategory'),
    # path('delete/<int:id>/', DeleteCategory, name='DeleteCategory'),
    # path('update/<int:id>/', UpdateCategory, name='UpdateCategory'),
]
