from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from .forms import formularioNovaDemanda
from django.http import HttpResponse

@login_required(redirect_field_name='login')
def projetos (request):
    return render(request, 'projetos.html')


@login_required(redirect_field_name='login')
def index(request):
    return render(request,'index.html')

@login_required(redirect_field_name='login')
def novo_demanda(request):
    return render(request,'demandas.html')


@login_required(redirect_field_name='login')
def cronograma(request):
    return render(request,'cronograma.html')


@login_required(redirect_field_name='login')
def recurso(request):
    return render(request,'recursos.html')

@login_required(redirect_field_name='login')
def painel(request):
    return render(request,'painel.html')

@login_required(redirect_field_name='login')
def resultado(request):
    return render(request,'resultado.html')


@login_required(redirect_field_name='login')
def admin(request):
    return render(request,'admin.html')

@login_required(redirect_field_name='login')
def novo_projeto(request):
    return render(request,'cadastro_projeto.html')


