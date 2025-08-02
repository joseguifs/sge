from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','category','brand','description','serial_number','cost_price','selling_price']
        widgets = {
            'title':forms.TextInput({'class':'form-control'}),
            'category':forms.Select({'class':'form-control','raws':3}),
            'brand':forms.Select({'class':'form-control','raws':3}),
            'description':forms.Textarea({'class':'form-control','raws':3}),
            'serial_number':forms.Textarea({'class':'form-control','raws':3}),
            'cost_price':forms.NumberInput({'class':'form-control','raws':3}),
            'selling_price':forms.NumberInput({'class':'form-control','raws':3})
        }
        labels = {
            'title':'Título',
            'category':'Categoria',
            'brand':'Marca',
            'description':'Descrição',
            'serial_number':'Número de série',
            'cost_price':'Preço de custo',
            'selling_price':'Preço de savenda',
        }