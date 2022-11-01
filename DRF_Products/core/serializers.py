from .models import Product, Brand
from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['brand']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "brand"]


class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(queryset=Brand.objects.all(), slug_field="brand", many=False)

    class Meta:
        model = Product
        fields = ["id", "name", "price", "brand"]
