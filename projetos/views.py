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
        descricao_projeto = request.POST.get('descricao_projeto')
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
                    descricao_projeto = descricao_projeto,
                
                    )
    

        if NovoProjeto.objects.filter(nome_projeto_id=nome_projeto_id).exists():
            messages.add_message(request, constants.ERROR, 'Projeto já cadastrado!')
            return redirect('novo_projeto')
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
    limpar_filtros = request.GET.get('limpar_filtros')
    fase_projeto_filtrar = request.GET.get('fase_projeto_filtrar')

    projeto = NovoProjeto.objects.all()
    status_projeto = StatusProjeto.objects.all()
    fase_projeto = FaseProjeto.objects.all()

    if limpar_filtros:
        nome_projeto_filtrar = ''
        status_projeto_filtrar = ''

    if nome_projeto_filtrar:
        projeto = projeto.filter(nome_projeto__nome__icontains=nome_projeto_filtrar)
    
    if status_projeto_filtrar:
        projeto = projeto.filter(status_id=status_projeto_filtrar)

    if status_projeto_filtrar:
        projeto = projeto.filter(fase_id=fase_projeto_filtrar)

    

    return render(request, 'projetos.html', {'projeto': projeto,
                                             'status_projeto': status_projeto,
                                             'fase_projeto': fase_projeto})


@login_required(redirect_field_name='login')
def projeto_unico (request, id):
    projeto_unico = get_object_or_404(NovoProjeto, id=id)
    # demanda_unica = get_object_or_404(NovaDemanda, id=id)
    status = StatusProjeto.objects.all()
    faseprojeto = FaseProjeto.objects.all()

    projetos = NovoProjeto.objects.all()

    return render(request, 'projeto_unico.html', {'projeto': projeto_unico,
                                                 'projetos':projetos,
                                                 'status': status,
                                                 'faseprojeto':faseprojeto
                                                 })

@login_required(redirect_field_name='login')

def editar_projeto(request, id):
    projeto = get_object_or_404(NovoProjeto, id=id)
    status = StatusProjeto.objects.all()
    faseprojeto = FaseProjeto.objects.all()
    
    if request.method == 'POST':
        # processar o formulário de atualização e salvar as mudanças no banco de dados
        # redirecionar o usuário para a página de detalhes do projeto atualizado
        descricao_projeto = request.POST.get('descricao_projeto')
        status_id = request.POST.get('statusprojeto')
        fase_id = request.POST.get('faseprojeto')
        prioridade = request.POST.get('prioridade')

        projeto = NovoProjeto(
                    projeto_id = id,
                    descricao_projeto = descricao_projeto,
                    status_id = status_id,
                    fase_id  = fase_id,
                    prioridade = prioridade,                
                    )
        
        projeto.save()        
        return render(request, f'projeto_unico/{id}.html')
        # try:
        #     projeto.save()
        #     messages.add_message(request, constants.SUCCESS, 'Projeto atualizado com sucesso!')
        #     return redirect('novo_projeto')
        # except:
        #     messages.add_message(request, constants.ERROR, 'Projeto não atualizado! Verifique os parametros digitados!' )
        #     return redirect('novo_projeto')

            # renderizar o formulário de atualização do projeto com os dados atuais
    return render(request, 'editar_projeto.html', {'projeto': projeto,
                                                   'status': status,
                                                   'faseprojeto':faseprojeto,                                                
                                                   
                                                   })

    

# @login_required(redirect_field_name='login')
# def index(request):
#     return render(request,'index.html')

# @login_required(redirect_field_name='login')
# def cronograma(request):
#     return render(request,'cronograma.html')



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