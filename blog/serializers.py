from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name', 'price', 'quantity', 'comment')


class ProductNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']

