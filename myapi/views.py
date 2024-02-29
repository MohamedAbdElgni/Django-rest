from django.http import HttpResponse
from django.shortcuts import render
from myapi.serializers import ProductSerializer
from rest_framework.response import Response
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework import status



@api_view(['GET'])
def prouducts_list_fun(request):
    
    prouducts_list = Product.objects.all()
    serializer = ProductSerializer(prouducts_list, many=True)
        
    
    return Response(serializer.data)


@api_view(['GET'])
def product_detail_fun(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data , status=200)


@api_view(['POST'])
def product_create_fun(request):
    serializer = ProductSerializer(data=request.data)
    
    if serializer.is_valid():
        print('serializer is valid')
        print('serializer is', serializer.validated_data)
        serializer.save()
        return Response(serializer.data , status=200)
    else:
        print('serializer is', serializer.validated_data)
        return Response(serializer.errors, status=400)
    


@api_view(['DELETE'])
def product_delete_fun(request, pk):
    if request.method == 'DELETE':
        product = Product.objects.get(id=pk)
        product.delete()
        return Response('Product deleted successfully', status=200)
    else:
        return Response('Product not found', status=404)



@api_view(['POST'])
def product_update_fun(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=200)
    else:
        
        return Response(serializer.errors, status=400)


