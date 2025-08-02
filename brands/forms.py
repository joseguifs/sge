from django import forms
from .models import Brand


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name','description']
        widgets = {
            'name':forms.TextInput({'class':'form-control'}),
            'description':forms.Textarea({'class':'form-control','raws':3})
        }
        labels = {
            'name':'Nome',
            'description':'Descrição'
        }