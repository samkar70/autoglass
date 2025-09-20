from django import forms
from .models import Orden

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['cliente_nombre', 'cliente_telefono', 'vehiculo', 'descripcion_servicio']
