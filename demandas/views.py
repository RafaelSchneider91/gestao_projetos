from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import formularioNovaDemanda
from django.http import HttpResponse


@login_required(redirect_field_name='login')
def novo_demanda(request):
    return render(request,'demandas.html')

### nova demanda
@login_required(redirect_field_name='login')
def cadastro_novademanda(request):
    form = formularioNovaDemanda()
    return render(request,'cadastro_novademanda.html', {'form':form})

@login_required(redirect_field_name='login')
def processa_cadastro_novademanda(request):
    form = formularioNovaDemanda(request.POST)
    if form.is_valid():
        form.save()
        return render(request,'processa_cadastro_novademanda.html')
    return HttpResponse('erro interno do sistema!')


