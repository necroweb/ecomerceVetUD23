from .models import Producto, Cliente, Carrito, Categoria

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from rest_framework.serializers import (
SerializerMethodField
)
from rest_framework import serializers

class ProductosSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class CarritoSerializer(ModelSerializer):
    carritoProducto = ProductosSerializer(many=True)
    class Meta:
        model = Carrito
        fields = '__all__'