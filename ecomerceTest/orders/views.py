from django.shortcuts import render
from .models import Producto, Cliente, Carrito, Categoria
from rest_framework.generics import ListAPIView
from .serializers import ProductosSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
#from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView,UpdateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView
#from .serializers import ProductoSerializer

@permission_classes((AllowAny,))
class ProductoListApi(ListAPIView):
    serializer_class = ProductosSerializer
    queryset = Producto.objects.all().order_by('nameProducto')
#    queryset = Producto.objects.filter(id_categoria=1).order_by('id')


# Create your views here.   


    # GenericAPIView

#def members(request):
    #return HttpResponse("Hello world!")

