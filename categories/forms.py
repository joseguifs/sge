from django import forms
from .models import Categorie


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['name','description']
        widgets = {
            'name':forms.TextInput({'class':'form-control'}),
            'description':forms.Textarea({'class':'form-control','raws':3})
        }
        labels = {
            'name':'Nome',
            'description':'Descrição'
        }