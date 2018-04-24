from django.contrib import admin
from .models import Cliente, Proveedor, Gasto, Ingreso

admin.site.register(Cliente),
admin.site.register(Proveedor),
admin.site.register(Gasto),
admin.site.register(Ingreso),