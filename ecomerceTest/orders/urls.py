from django.urls import re_path
from .views import ProductoListApi


app_name = 'orders'

urlpatterns = [
re_path(r"^getproducto$",ProductoListApi.as_view(), name="getproducto"),
]