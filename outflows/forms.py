from django import forms
from .models import Outflows


class OutflowForm(forms.ModelForm):
    class Meta:
        model = Outflows
        fields = ['product','quantity','description']
        widgets = {
            'product':forms.Select({'class':'form-control'}),
            'quantity':forms.NumberInput({'class':'form-control'}),
            'description':forms.Textarea({'class':'form-control','raws':3})
        }
        labels = {
            'product':'Produto',
            'quantity':'Quantidade',
            'description':'Descrição'
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product') # campo que está relacionado a outro obj e podemos acessar seus campos

        if quantity > product.quantity:
            raise forms.ValidationError(f"Quantidade em estoque para o produto {product.title} é {product.quantity}")
        return quantity;
'''
    objetos que tem um campo como de chave estrangeira, onotone, manytomany são campos de objetos que estão relacionados a outros objetos, logo se pegarmos o valor desse campo (com get no caso de validação) estamos na verdade pegando o objeto relacionado a ele, podendo acesar atributos desse objeto, e quando criamos um forms, campos do tipo mencionados serão selects para  objetos, mas oq o user verá será o __str__ dos objetos.Portanto todas as opções do campo são basicamentes objetos mas na exibição do formato __str__
'''