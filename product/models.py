from django.db import models
from category.models import SubCategory

# Create your models here.
class ProductRu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Product (RU)'
        verbose_name_plural = 'Products (RU)'
        
    def __str__(self) -> str:
        return self.name
        
class ImagesRu(models.Model):
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    product = models.ForeignKey(ProductRu, on_delete=models.CASCADE, related_name='images')
    def __str__(self) -> str:
        return self.product
    
    
    
class ProductUz(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Product (UZ)'
        verbose_name_plural = 'Products (UZ)'
        
    def __str__(self) -> str:
        return self.name
        
class ImagesUz(models.Model):
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    product = models.ForeignKey(ProductUz, on_delete=models.CASCADE, related_name='images')
    def __str__(self) -> str:
        return self.product