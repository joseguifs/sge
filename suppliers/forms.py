from django import forms
from .models import Suppliers


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = ['name','description']
        widgets = {
            'name':forms.TextInput({'class':'form-control'}),
            'description':forms.Textarea({'class':'form-control','raws':3})
        }
        labels = {
            'name':'Nome',
            'description':'Descrição'
        }