from django.shortcuts import render
from .models import Category, SubCategory
from rest_framework import generics
from .serializers import CategorySerializer, SubCategorySerializer, CategoryCreateSerializer, SubCategoryCreateSerializer

# Create your views here.
# Categories
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    
class CategoryEdit(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    
class CategoryDelete(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    
    
# SubCategories
class SubCategoryList(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    
class SubCategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = SubCategoryCreateSerializer
    
class SubCategoryEdit(generics.UpdateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryCreateSerializer
    
class SubCategoryDelete(generics.DestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryCreateSerializer