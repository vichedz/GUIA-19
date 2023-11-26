from django import forms
from ..models import Productos


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'stock', 'fk_prov']
