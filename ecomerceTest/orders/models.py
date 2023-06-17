from django.db import models
# extende los max_length 
# error method POST fechas -- no enlista las FECHAS citas
# incluir una CLASS CATEGORIA ----------->>>

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.IntegerField(unique=True)
    nameCliente = models.CharField( max_length=50, default='')
    email = models.EmailField(null=False)
    tel = models.IntegerField(null=False)
    direccion = models.CharField(max_length=50, default='')
    Barrio = models.CharField( max_length=50, default='')

    def __str__(self):
        return f'Cliente ({self.id}): {self.nameCliente} {self.email}'

    class meta: 
        db_table='clientes'
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
        ordering=['Cliente']        


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nameProducto = models.CharField(max_length=50, default='')
    precioCompra = models.IntegerField( null=True)
    precioVenta = models.IntegerField( null=True)
    proveedor = models.CharField(max_length=50, default='')
    existencia = models.BooleanField(null=True)
    
    
    def __str__(self):
        return f'Producto ({self.id}): {self.nameProducto} {self.precioVenta}'

    class meta:
        db_table='producto' 
        verbose_name='Producto'
        verbose_name_plural='Productos'
        ordering=['Producto']

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nameCategoria = models.CharField(max_length=50, default='')        
    descripcion = models.CharField(max_length=50, default='')

    def __str__(self) -> str:
        return f'Categoria ({self.id}): {self.nameCategoria} {self.descripcion}'

    class meta:
        db_table='categoria' 
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['Categorias']
    

class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    carritoCliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    carritoProducto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    carritoCategoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    precioTotal = models.IntegerField(null=True)

    
    def __str__(self):
        return f'Categoria ({self.id}): {self.carritoCliente} {self.carritoProducto} {self.precioTotal}'

    class meta:
        db_table='carrito' 
        verbose_name='Carrito'