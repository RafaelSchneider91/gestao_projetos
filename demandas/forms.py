from django import forms
from . models import NovaDemanda

class formularioNovaDemanda(forms.ModelForm):
    class Meta:
        model = NovaDemanda
        # fields = ('nome', 
        #           'descricao',
        #           'categoria',
        #           'setor',
        #           'nome_solicitante',
        #           'retorno_financeiro',
        #           'base_calculo_retorno',
        #           'retorno_qualitativo',
        #           'link_analise',
        #           'observacao',
        #           'status',
        #           'usuario_criacao',
        #           )
        exclude = ('data_cadastro',
                   )


        # fields = '__all__'
        