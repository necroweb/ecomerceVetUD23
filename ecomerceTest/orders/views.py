from django.shortcuts import render
from .models import Producto, Cliente, Carrito, Categoria
from rest_framework.generics import ListAPIView
from .serializers import ProductosSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView,UpdateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView
from django.views.generic import ListView
# httpResponse 
#from django.http import HttpResponse


#from .serializers import ProductoSerializer

#Permission_classes(allow)
@permission_classes((AllowAny,))
class ProductoListApi(ListAPIView):
    serializer_class = ProductosSerializer
    queryset = Producto.objects.all().order_by('nameProducto')

class  OrdersCreateAPIView(CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer

#create view with HttpResonpe
#def index(response, id):
    #ls=Producto.objects.get(id=id)
    #return render(response,"template/home.html",{})
#    return HttpResponse("<h1>Hola mundo!</h1>")

# reques para hacer peticion de view
def home (request):
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos': productos}
    )

    