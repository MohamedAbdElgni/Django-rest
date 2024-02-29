from django.http import HttpResponse
from django.shortcuts import render
from myapi.serializers import ProductSerializer
from rest_framework.response import Response
from products.models import Product
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def prouducts_list_fun(request):
    
    prouducts_list = Product.objects.all()
    serializer = ProductSerializer(prouducts_list, many=True)
        
    
    return Response(serializer.data)