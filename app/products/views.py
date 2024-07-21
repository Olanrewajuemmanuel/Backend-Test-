from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer
from core.permissions import IsAdminOrReadOnly


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    """This viewsets handles an authenticated user's product CRUD operations
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdminOrReadOnly,
    ]
