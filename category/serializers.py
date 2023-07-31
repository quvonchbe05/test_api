from rest_framework import serializers
from .models import Category, SubCategory
import json

def jsonga(arg):
    data = {}
    data['name_ru'] = arg.name_ru
    data['name_uz'] = arg.name_uz
    data['description_ru'] = arg.description_ru
    data['description_uz'] = arg.description_uz
    return json.dumps(data)
    

# Categories
class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()
    
    def get_subcategories(self, obj):
        return json.dumps([jsonga(subcategory) for subcategory in obj.subcategories.all()])

    class Meta:
        model = Category
        fields = ('id', 'name_ru', 'name_uz', 'description_ru', 'description_uz', 'subcategories')
        
        
        
class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name_ru', 'name_uz', 'description_ru', 'description_uz')



# SubCategories
class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = ('id', 'name_ru', 'name_uz', 'description_ru', 'description_uz', 'category')
        
        
class SubCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'name_ru', 'name_uz', 'description_ru', 'description_uz', 'category')