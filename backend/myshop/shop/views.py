from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Product, Citems
from .serializers import ProductSerializer, CitemsSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CitemsViewSet(viewsets.ModelViewSet):
    queryset = Citems.objects.all()
    serializer_class = CitemsSerializer
