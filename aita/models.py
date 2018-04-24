from django.db import models

class Proveedor(models.Model):
	nombre    = models.CharField(max_length=50)
	direccion = models.TextField(null=True)
	cif       = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['nombre']

class Cliente(models.Model):
	nombre    = models.CharField(max_length=50)
	direccion = models.TextField(null=True)
	cif       = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['nombre']

class Gasto (models.Model):
	proveedor      = models.ForeignKey (Proveedor, on_delete=models.PROTECT)
	tipo           = models.CharField(max_length=50, null=True)
	n_factura      = models.CharField(max_length=50)
	fecha          = models.DateField()
	base_imponible = models.DecimalField(max_digits=6, decimal_places=2)
	iva            = models.DecimalField(max_digits=6, decimal_places=2)
	total          = models.DecimalField(max_digits=6, decimal_places=2, null=True)

	class Meta:
		ordering = ['-fecha']

class Ingreso (models.Model):
	cliente        = models.ForeignKey (Cliente, on_delete=models.PROTECT)
	tipo           = models.CharField(max_length=50, null=True)
	n_factura      = models.CharField(max_length=50)
	fecha          = models.DateField()
	base_imponible = models.DecimalField(max_digits=6, decimal_places=2)
	iva            = models.DecimalField(max_digits=6, decimal_places=2)
	total          = models.DecimalField(max_digits=6, decimal_places=2, null=True)

	class Meta:
		ordering = ['-fecha']