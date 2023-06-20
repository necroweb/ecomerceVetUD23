from django.urls import re_path
from . import views
from .views import ProductoListApi, OrdersCreateAPIView

app_name = 'orders'

urlpatterns = [
re_path(r"^getproducto$",ProductoListApi.as_view(), name="getproducto"),
re_path(r"^createOrders$", OrdersCreateAPIView.as_view(), name="getproducto"),

]

