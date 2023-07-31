from django.urls import path
from .views import (
    CategoryList, 
    CategoryCreate,
    CategoryEdit,
    CategoryDelete,
    SubCategoryList,
    SubCategoryCreate,
    SubCategoryEdit,
    SubCategoryDelete,
)

urlpatterns = [
    # Categories
    path('categories/list/', CategoryList.as_view()),
    path('categories/create/', CategoryCreate.as_view()),
    path('categories/edit/<int:pk>', CategoryEdit.as_view()),
    path('categories/delete/<int:pk>', CategoryDelete.as_view()),
    # SubCategories
    path('subcategories/list/', SubCategoryList.as_view()),
    path('subcategories/create/', SubCategoryCreate.as_view()),
    path('subcategories/edit/<int:pk>', SubCategoryEdit.as_view()),
    path('subcategories/delete/<int:pk>', SubCategoryDelete.as_view()),
]