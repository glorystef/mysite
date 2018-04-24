from django.shortcuts import render
from .forms import GastoForm, IngresoForm, ClienteForm, ProveedorForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Gasto, Ingreso
import datetime
from datetime import date
import json

#menu inincial
def index(request):
	return render(request, 'index.html')

#vista para crear gasto
def crear_gasto(request):
	form = GastoForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		form.save()
		form.instance.total = form.instance.base_imponible*(1+(form.instance.iva/100))
		form.save()
		return HttpResponseRedirect(reverse('aita:nuevo-gasto'))
	return render(request, 'gasto.html', {'form':form})

#vista para crear ingreso
def crear_ingreso(request):
	form = IngresoForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		form.save()
		form.instance.total = form.instance.base_imponible*(1+(form.instance.iva/100))
		form.save()
		return HttpResponseRedirect(reverse('aita:nuevo-ingreso'))
	return render(request, 'ingreso.html', {'form':form})

#vista para crear cliente
def crear_cliente(request):
	form = ClienteForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('aita:nuevo-ingreso'))
	return render(request, 'cliente.html', {'form':form})

#vista para crear proveedor
def crear_proveedor(request):
	form = ProveedorForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('aita:nuevo-gasto'))
	return render(request, 'proveedor.html', {'form':form})

#tabla
def tabla(request):
	objects = Ingreso.objects.all()
	today = datetime.date.today()
	mes = today.month
	año = today.year
	if mes == 1 or mes == 2 or mes == 3:
		ingreso = Ingreso.objects.filter(fecha__gte=date(year=año,month=1,day=1), fecha__lt=date(year=año,month=4,day=1))
		gasto = Gasto.objects.filter(fecha__gte=date(year=año,month=1,day=1), fecha__lt=date(year=año,month=4,day=1))
	elif mes == 4 or mes == 5 or mes == 6:
		ingreso = Ingreso.objects.filter(fecha__gte=date(year=año,month=4,day=1), fecha__lt=date(year=año,month=7,day=1))
		gasto = Gasto.objects.filter(fecha__gte=date(year=año,month=4,day=1), fecha__lt=date(year=año,month=7,day=1))
	elif mes == 7 or mes == 8 or mes == 9:
		ingreso = Ingreso.objects.filter(fecha__gte=date(year=año,month=7,day=1), fecha__lt=date(year=año,month=10,day=1))
		gasto = Gasto.objects.filter(fecha__gte=date(year=año,month=7,day=1), fecha__lt=date(year=año,month=10,day=1))
	elif mes == 10 or mes == 11 or mes == 12:
		ingreso_actual = Ingreso.objects.filter(fecha__gte=date(year=año,month=10,day=1), fecha__lt=date(year=año+1,month=1,day=1))
		gasto_actual = Gasto.objects.filter(fecha__gte=date(year=año,month=10,day=1), fecha__lt=date(year=año+1,month=1,day=1))
	sum_ingreso = 0
	for i in ingreso:
		sum_ingreso = sum_ingreso + i.total
	sum_gasto = 0
	for g in gasto:
		sum_gasto = sum_gasto + g.total
	balance = sum_ingreso - sum_gasto
	return render(request, 'tabla.html', {'ingreso':ingreso,'gasto':gasto,'sum_ingreso':sum_ingreso,'sum_gasto':sum_gasto,\
		'balance':balance})

#tabla trimestre anterior
def tabla_anterior(request):
	objects = Ingreso.objects.all()
	today = datetime.date.today()
	mes = today.month
	año = today.year
	if mes == 1 or mes == 2 or mes == 3:
		ingreso = Ingreso.objects.filter(fecha__gte=date(year=año-1,month=10,day=1), fecha__lt=date(year=año,month=1,day=1))
		gasto = Gasto.objects.filter(fecha__gte=date(year=año-1,month=10,day=1), fecha__lt=date(year=año,month=1,day=1))
	elif mes == 4 or mes == 5 or mes == 6:
		ingreso = Ingreso.objects.filter(fecha__gte=date(year=año,month=1,day=1), fecha__lt=date(year=año,month=4,day=1))
		gasto = Gasto.objects.filter(fecha__gte=date(year=año,month=1,day=1), fecha__lt=date(year=año,month=4,day=1))
	elif mes == 7 or mes == 8 or mes == 9:
		ingreso = Ingreso.objects.filter(fecha__gte=date(year=año,month=4,day=1), fecha__lt=date(year=año,month=7,day=1))
		gasto = Gasto.objects.filter(fecha__gte=date(year=año,month=4,day=1), fecha__lt=date(year=año,month=7,day=1))
	elif mes == 10 or mes == 11 or mes == 12:
		ingreso = Ingreso.objects.filter(fecha__gte=date(year=año,month=7,day=1), fecha__lt=date(year=año,month=10,day=1))
		gasto = Gasto.objects.filter(fecha__gte=date(year=año,month=7,day=1), fecha__lt=date(year=año,month=10,day=1))
	sum_ingreso = 0
	for i in ingreso:
		sum_ingreso = sum_ingreso + i.total
	sum_gasto = 0
	for g in gasto:
		sum_gasto = sum_gasto + g.total
	balance = sum_ingreso - sum_gasto
	return render(request, 'tabla.html', {'ingreso':ingreso,'gasto':gasto,'sum_ingreso':sum_ingreso,'sum_gasto':sum_gasto,\
		'balance':balance})

#vista grafico evolucion
def evolucion(request):
	form = "asier"
	today = datetime.date.today()
	mes = today.month
	año = today.year
	gasto_list = []
	ingreso_list = []
	timeline = []
	if mes >= 6:
		for h in range(mes-5,mes,+1):
			ingreso = Ingreso.objects.filter(fecha__month=h, fecha__year=año)
			sum_ingreso = 0
			for i in ingreso:
				sum_ingreso = sum_ingreso + i.total
			sum_ingreso = float("{:.2f}".format(sum_ingreso))
			ingreso_list.append(sum_ingreso)
			gasto = Gasto.objects.filter(fecha__month=h, fecha__year=año)
			sum_gasto = 0
			for g in gasto:
				sum_gasto = sum_gasto + g.total
			sum_gasto = float("{:.2f}".format(sum_gasto))
			gasto_list.append(sum_gasto)
			fecha = date(year=año, month=h,day=1)
			timeline.append(fecha.strftime("%m/%y"))
	else:
		for h in range(7+mes,13,+1):
			ingreso = Ingreso.objects.filter(fecha__month=h, fecha__year=año-1)
			sum_ingreso = 0
			for i in ingreso:
				sum_ingreso = sum_ingreso + i.total
			sum_ingreso = float("{:.2f}".format(sum_ingreso))
			ingreso_list.append(sum_ingreso)
			gasto = Gasto.objects.filter(fecha__month=h, fecha__year=año-1)
			sum_gasto = 0
			for g in gasto:
				sum_gasto = sum_gasto + g.total
			sum_gasto = float("{:.2f}".format(sum_gasto))
			gasto_list.append(sum_gasto)
			fecha = date(year=año-1, month=h,day=1)
			timeline.append(fecha.strftime("%m/%y"))
		for h in range(1,mes+1,+1):
			ingreso = Ingreso.objects.filter(fecha__month=h, fecha__year=año)
			sum_ingreso = 0
			for i in ingreso:
				sum_ingreso = sum_ingreso + i.total
			sum_ingreso = float("{:.2f}".format(sum_ingreso))
			ingreso_list.append(sum_ingreso)
			gasto = Gasto.objects.filter(fecha__month=h, fecha__year=año)
			sum_gasto = 0
			for g in gasto:
				sum_gasto = sum_gasto + g.total
			sum_gasto = float("{:.2f}".format(sum_gasto))
			gasto_list.append(sum_gasto)
			fecha = date(year=año, month=h,day=1)
			timeline.append(fecha.strftime("%m/%y"))
	json_timeline = json.dumps(timeline)
	print (timeline)
	return render(request, 'evolucion.html', {'ingreso_list':ingreso_list,'gasto_list':gasto_list,'timeline':json_timeline})