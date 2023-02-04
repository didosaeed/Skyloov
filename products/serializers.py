from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductSearchSerializer(serializers.Serializer):
    category = serializers.CharField()
    brand = serializers.CharField()
    min_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    max_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    min_quantity = serializers.IntegerField()
    max_quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField()
