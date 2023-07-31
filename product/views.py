from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductRuSerializer, ProductUzSerializer
from .models import ProductRu, ProductUz

# Create your views here.
class ProductRuList(generics.ListAPIView):
    queryset = ProductRu.objects.all()
    serializer_class = ProductRuSerializer
    
    
    
class ProductUzList(generics.ListAPIView):
    queryset = ProductUz.objects.all()
    serializer_class = ProductUzSerializer