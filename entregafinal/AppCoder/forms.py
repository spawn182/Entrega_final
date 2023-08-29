from django import forms

class Cursoform(forms.Form):
    nombre = forms.CharField(max_length=50)
    comision = forms.IntegerField()

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=50)
    
class EstudiantesForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()


class EntregablesForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField()     
