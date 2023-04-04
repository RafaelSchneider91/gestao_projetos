from django import forms
from . models import NovaDemanda

class formularioNovaDemanda(forms.ModelForm):
    class Meta:
        model = NovaDemanda
        fields = ('nome', 'descricao')
        
