from rest_framework import serializers
from .models import Product, Citems

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CitemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citems
        fields = '__all__'
