from django.contrib import admin
from .models import ProductRu, ProductUz, ImagesRu, ImagesUz

# Register your models here.
admin.site.register(ProductRu)
admin.site.register(ProductUz)
admin.site.register(ImagesRu)
admin.site.register(ImagesUz)