from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^index$', login_required(views.index), name='index'),
	url(r'^nuevo_gasto$', login_required(views.crear_gasto), name='nuevo-gasto'),
	url(r'^nuevo_ingreso$', login_required(views.crear_ingreso), name='nuevo-ingreso'),
	url(r'^nuevo_proveedor$', login_required(views.crear_proveedor), name='nuevo-proveedor'),
	url(r'^nuevo_cliente$', login_required(views.crear_cliente), name='nuevo-cliente'),
	url(r'^tabla$', login_required(views.tabla), name='tabla'),
	url(r'^tabla_anterior$', login_required(views.tabla_anterior), name='tabla-anterior'),
	url(r'^evolucion$', login_required(views.evolucion), name='evolucion'),
	]