from django import forms
from .models import Gasto, Ingreso, Cliente, Proveedor
from django.forms import ModelForm, Textarea

class GastoForm(forms.ModelForm):
	class Meta:
		model = Gasto
		fields = [
			'proveedor',
			'tipo',
			'n_factura',
			'fecha',
			'base_imponible',
			'iva',
		]
		widgets = {
			'proveedor':forms.Select(attrs={'class':'form-control'}),
			'tipo':forms.TextInput(attrs={'class':'form-control'}),
			'n_factura':forms.TextInput(attrs={'class':'form-control'}),
			'fecha':forms.TextInput(attrs={'class':'form-control'}),
			'base_imponible':forms.TextInput(attrs={'class':'form-control'}),
			'iva':forms.TextInput(attrs={'class':'form-control'}),
		}

class IngresoForm(forms.ModelForm):
	class Meta:
		model = Ingreso
		fields = [
			'cliente',
			'tipo',
			'n_factura',
			'fecha',
			'base_imponible',
			'iva',
		]
		widgets = {
			'cliente':forms.Select(attrs={'class':'form-control'}),
			'tipo':forms.TextInput(attrs={'class':'form-control'}),
			'n_factura':forms.TextInput(attrs={'class':'form-control'}),
			'fecha':forms.TextInput(attrs={'class':'datepicker form-control'}),
			'base_imponible':forms.TextInput(attrs={'class':'form-control'}),
			'iva':forms.TextInput(attrs={'class':'form-control'}),
		}

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = [
			'nombre',
			'direccion',
			'cif',
		]
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'direccion':forms.Textarea(attrs={'class':'form-control'}),
			'cif':forms.TextInput(attrs={'class':'form-control'}),
		}

class ProveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedor
		fields = [
			'nombre',
			'direccion',
			'cif',
		]
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'direccion':forms.Textarea(attrs={'class':'form-control'}),
			'cif':forms.TextInput(attrs={'class':'form-control'}),
		}