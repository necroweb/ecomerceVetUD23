from django.contrib import admin
from .models import Producto
from .models import Cliente 
from .models import Carrito
from .models import Categoria

# Register your models here.
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Carrito)
admin.site.register(Categoria)