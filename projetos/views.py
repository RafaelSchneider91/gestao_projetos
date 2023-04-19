from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse
from demandas.models import NovaDemanda
from projetos.models import StatusProjeto, FaseProjeto, NovoProjeto

@login_required(redirect_field_name='login')
def novo_projeto(request):
    if request.method == "GET":
    # form = FormularioNovoProjeto()
        demandas = NovaDemanda.objects.all()
        statusprojeto = StatusProjeto.objects.all()
        faseprojeto = FaseProjeto.objects.all()
        equipes = User.objects.all()

        return render(request,'cadastro_projeto.html', {'demandas':demandas, #TODO: filtrar demanda que estão em aberto.
                                                        'statusprojeto':statusprojeto,
                                                        'faseprojeto':faseprojeto,
                                                        'equipes':equipes
                                                        }) 
    elif request.method == "POST":
        nome_projeto_id = request.POST.get('nomeprojeto')
        status_id = request.POST.get('statusprojeto')
        fase_id = request.POST.get('faseprojeto')

        if request.POST.get('staramais') == None:    
            staramais = False
        else:
            staramais = True
        
        if request.POST.get('staralabs') == None:
            staralabs = False
        else:
            staralabs = True
        
        prioridade = request.POST.get('prioridade')
        user_id = request.POST.getlist('equipe')

     
        # demanda_id = request.POST.get('nomeprojeto')
        # demanda = NovaDemanda.objects.get(id=demanda_id)

        projeto = NovoProjeto(nome_projeto_id = nome_projeto_id,
                    status_id = status_id,
                    fase_id  = fase_id,
                    staramais = staramais,
                    staralabs = staralabs,
                    prioridade = prioridade,
                
                    )
        try:
            projeto.save()
            projeto.equipe.add(*user_id)
            projeto.save()
            messages.add_message(request, constants.SUCCESS, 'Projeto cadastrado com sucesso!')
            return redirect('novo_projeto')
        except:
            messages.add_message(request, constants.ERROR, 'Projeto não cadastrado! Verifique os parametros digitados!' )
            return redirect('novo_projeto')


@login_required(redirect_field_name='login')
def projetos (request):
    nome_projeto_filtrar = request.GET.get('nome_projeto_filtro')
    status_projeto_filtrar = request.GET.get('status_projeto_filtrar')

    projeto = NovoProjeto.objects.all()
    status_projeto = StatusProjeto.objects.all()
    
    if status_projeto_filtrar:
        projeto = projeto.filter(status_id=status_projeto_filtrar)

    if nome_projeto_filtrar:
        projeto = projeto.filter(nome_projeto__nome__icontains=nome_projeto_filtrar)

    
    return render(request, 'projetos.html', {'projeto': projeto,
                                             'status_projeto': status_projeto})


@login_required(redirect_field_name='login')
def projeto_unico (request, id):
    projeto_unico = get_object_or_404(NovoProjeto, id=id)

    projetos = NovoProjeto.objects.all()

    return render(request, 'projeto_unico.html', {'projeto': projeto_unico,
                                                 'projetos':projetos
                                                 })



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
def tarefa(request):
    return render(request,'tarefa.html')

@login_required(redirect_field_name='login')
def resultado(request):
    return render(request,'resultado.html')








# @login_required(redirect_field_name='login')
# def processa_cadastro_novoprojeto(request):
#     formularionovoprojeto = FormularioNovoProjeto(request.POST)
#     # if form.is_valid():
#     formularionovoprojeto.save()
#     return render(request,'processa_cadastro_novoprojeto.html')
#     # return HttpResponse('erro interno do sistema!')