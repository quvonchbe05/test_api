from rest_framework import serializers
from .models import ProductRu, ImagesRu, ProductUz, ImagesUz

class ProductRuSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        return [image.image.url for image in obj.images.all()]

    class Meta:
        model = ProductRu
        fields = ('id', 'name', 'description', 'price', 'quantity', 'category', 'images')


class ProductUzSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        return [image.image.url for image in obj.images.all()]

    class Meta:
        model = ProductUz
        fields = ('id', 'name', 'description', 'price', 'quantity', 'category', 'images')