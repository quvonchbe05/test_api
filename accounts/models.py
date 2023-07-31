from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass




# from django.db import models


# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)

#     class Meta:
#         app_label = "categories"
#         verbose_name = "Category"
#         verbose_name_plural = "Categories"
        
#     def __str__(self) -> str:
#         return self.name


# class CategoryRu(Category):

#     class Meta:
#         app_label = "categories"
#         verbose_name = "Category (RU)"
#         verbose_name_plural = "Categories (RU)"


# class CategoryUz(Category):

#     class Meta:
#         app_label = "categories"
#         verbose_name = "Category (UZ)"
#         verbose_name_plural = "Categories (UZ)"
        
        
# class Subcategory(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     category = models.ForeignKey(
#         Category, on_delete=models.CASCADE, related_name="subcategories"
#     )

#     class Meta:
#         app_label = "categories"
#         ordering = ("name",)
        
#     def __str__(self) -> str:
#         return self.name


# class SubcategoryRu(Subcategory):

#     class Meta:
#         app_label = "categories"
#         verbose_name = "Subcategory (RU)"
#         verbose_name_plural = "Subcategories (RU)"


# class SubcategoryUz(Subcategory):

#     class Meta:
#         app_label = "categories"
#         verbose_name = "Subcategory (UZ)"
#         verbose_name_plural = "Subcategories (UZ)"