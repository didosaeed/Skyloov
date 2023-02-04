from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Product
from .serializers import ProductSerializer, ProductSearchSerializer


class ProductSearchView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ProductSerializer

    def get_queryset(self):
        serializer = ProductSearchSerializer(data=self.request.data)
        if serializer.is_valid():
            category = serializer.validated_data.get('category')
            brand = serializer.validated_data.get('brand')
            min_price = serializer.validated_data.get('min_price')
            max_price = serializer.validated_data.get('max_price')
            min_quantity = serializer.validated_data.get('min_quantity')
            max_quantity = serializer.validated_data.get('max_quantity')
            created_at = serializer.validated_data.get('created_at')

            queryset = Product.objects.filter(
                category__icontains=category,
                brand__icontains=brand,
                price__gte=min_price,
                price__lte=max_price,
                quantity__gte=min_quantity,
                quantity__lte=max_quantity,
                created_at__gte=created_at,
            )
            return queryset
        return Product.objects.none()
