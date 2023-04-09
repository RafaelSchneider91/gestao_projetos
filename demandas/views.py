from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# from .forms import formularioNovaDemanda
from django.http import HttpResponse
from demandas.models import NovaDemanda, Setor
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants


@login_required(redirect_field_name='login')
def novo_demanda(request):
    return render(request,'demandas.html')

### nova demanda
@login_required(redirect_field_name='login')
def cadastro_novademanda(request):
    if request.method == "GET":
        # form = formularioNovaDemanda()
        # status_backlog = StatusBacklog.objects.all()
        setores = Setor.objects.all()
        # user_id = request.user.id
        # # usuario_criacao = User.get_username()
        # # categoria_backlog = Categoria.objects.all()
        # print(user_id)
        
        return render(request,'cadastro_novademanda.html', {'setores': setores}) 
    
        
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        categoria  = request.POST.get('categoria')
        setor = request.POST.get('setor_demanda_id')
        nome_solicitante = request.POST.get('nome_solicitante')
        retorno_financeiro = request.POST.get('retorno_financeiro')
        base_calculo_retorno = request.POST.get('base_calculo_retorno')
        retorno_qualitativo = request.POST.get('retorno_qualitativo')
        link_analise = request.POST.get('link_analise')
        observacao = request.POST.get('observacao')
        status = request.POST.get('status')

        user_id = request.user.id
        usuario_criacao = User.objects.get(id = user_id)
        # usuario_criacao = usuario_criacao

        print(user_id)
        print(usuario_criacao)
        
        

        demandas = NovaDemanda(nome = nome,
                    descricao = descricao,
                    categoria  = categoria,
                    setor_demanda_id = setor,
                    nome_solicitante = nome_solicitante,
                    retorno_financeiro = retorno_financeiro,
                    base_calculo_retorno = base_calculo_retorno,
                    retorno_qualitativo = retorno_qualitativo,
                    link_analise = link_analise,
                    observacao = observacao,
                    status = status,
                    usuario_criacao_id = user_id
                    
                    )
        
        # user_id = request.user.id
        
        # usuario_criacao = User.objects.get(id=request.id)

    
        try:
            demandas.save()
            messages.add_message(request, constants.SUCCESS, 'Demanda cadastrada com sucesso!')
            return redirect('cadastro_novademanda')
        except:
            messages.add_message(request, constants.ERROR, 'Demanda não cadastrada! Verifique os parametros digitados!' )
            return redirect('cadastro_novademanda')


        # return HttpResponse('ok')





        


