from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


# Create your views here.

@api_view(['Get'])
def api_overview(request):
    api_urls = {
        'List': '/product/list',
        'Detail view': '/product/details/<int:id>',
        'Create': '/product/create/',
        'Delete': '/product/delete/<int:id>',
        'Update': '/product/update/<int:id>'
    }
    return Response(api_urls)


@api_view(['Get'])
def showall(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['Post'])
def createproduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
