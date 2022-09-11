from dataclasses import fields
from .models import *
from rest_framework import serializers

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    productimage = ProductImageSerializer(required=False, many=True)
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1