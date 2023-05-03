from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# from .forms import formularioNovaDemanda
from django.http import HttpResponse
from demandas.models import NovaDemanda, Setor
from projetos.models import NovoProjeto
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Q



@login_required(redirect_field_name='login')
def demandas_projeto(request):
    return render(request,'demandas_projeto.html')

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
        # categoria  = request.POST.get('categoria')
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
                    # categoria  = categoria,
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


@login_required(redirect_field_name='login')
def demandas(request):
    if request.method == "GET":
        nome_demanda_filtrar = request.GET.get('nome_demanda_filtro')
        limpar_filtros = request.GET.get('limpar_filtros')
        demandas = NovaDemanda.objects.all()
        projetos = NovoProjeto.objects.all()
        # print(projetos)


        demandas_sem_projeto = NovaDemanda.objects.exclude(novoprojeto__isnull=False)
        
        # print(demandas_sem_projeto)



        if limpar_filtros:
            nome_demanda_filtrar = ''


        if nome_demanda_filtrar:
            demandas = demandas.filter(nome__icontains=nome_demanda_filtrar)

        

        return render(request, 'demandas.html', {'demandas': demandas,
                                                'projetos': projetos,
                                                'demandas_sem_projeto':demandas_sem_projeto
                                                })
    elif request.method == "POST":
        status_modal = request.POST.get('status_modal')
        print(status_modal)

        demandas = NovaDemanda(status = status_modal) #TODO: verificar como salvar a alteração;
           
        demandas.save()
        return redirect('demandas')


@login_required(redirect_field_name='login')
def demanda_unico (request, id):
    demanda_unico = get_object_or_404(NovaDemanda, id=id)
    # demanda_unica = NovaDemanda.objects.get(id=)
    # status = StatusProjeto.objects.all()
    # faseprojeto = FaseProjeto.objects.all()

    demandas = NovaDemanda.objects.all()

    return render(request, 'demanda_unico.html', {'demanda': demanda_unico,
                                                 'demandas':demandas,
                                                 })

        


