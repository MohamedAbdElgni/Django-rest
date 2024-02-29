
import os
from django.urls import path
from .views import *
urlpatterns = [
    path('prod-list-fun/', prouducts_list_fun, name='prod-list-fun'),
    path('prod-detail-fun/<str:pk>/', product_detail_fun, name='prod-detail-fun'),
    path('prod-create-fun/', product_create_fun, name='prod-create-fun'),
    path('prod-update-fun/<str:pk>/', product_update_fun, name='prod-update-fun'),
    path('prod-delete-fun/<str:pk>/', product_delete_fun, name='prod-delete-fun'),
    
    
]