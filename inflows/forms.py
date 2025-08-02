from django import forms
from .models import Inflow


class InflowForm(forms.ModelForm):
    class Meta:
        model = Inflow
        fields = ['supplier','product','quantity','description']
        widgets = {
            'supplier':forms.Select({'class':'form-control'}),
            'product':forms.Select({'class':'form-control'}),
            'quantity':forms.NumberInput({'class':'form-control'}),
            'description':forms.Textarea({'class':'form-control','raws':3})
        }
        labels = {
            'supplier':'Fornecedor',
            'product':'Produto',
            'quantity':'Quantidade',
            'description':'Descrição'
        }