from django import forms 

class CafeFormulario (forms.Form):
    nombre=forms.CharField(max_length=20)
    precio=forms.IntegerField()

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=20)