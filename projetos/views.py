from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from django.urls import reverse
from demandas.models import NovaDemanda
from projetos.models import StatusProjeto, FaseProjeto, NovoProjeto, PerfilUsuarios, UsuariosProjeto

@login_required(redirect_field_name='login')
def novo_projeto(request):
    if request.method == "GET":
    # form = FormularioNovoProjeto()
        demandas = NovaDemanda.objects.all()
        statusprojeto = StatusProjeto.objects.all()
        faseprojeto = FaseProjeto.objects.all()
        usuarios = User.objects.all()
        perfis = PerfilUsuarios.objects.all()

        return render(request,'cadastro_projeto.html', {'demandas':demandas, #TODO: filtrar demanda que estão em aberto.
                                                        'statusprojeto':statusprojeto,
                                                        'faseprojeto':faseprojeto,
                                                        'usuarios':usuarios,
                                                        'perfis': perfis
                                                        })
    
    elif request.method == "POST":
        nome_projeto_id = request.POST.get('nomeprojeto')
        descricao_projeto = request.POST.get('descricao_projeto')
        status_id = request.POST.get('statusprojeto')
        fase_id = request.POST.get('faseprojeto')
        categoria  = request.POST.get('categoria')


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
                    categoria  = categoria,
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


def usuarios_projeto(request, id):
    corpo = request.body
    print(corpo)
    return JsonResponse({'teste': 'teste'})





    # projeto = NovoProjeto.objects.filter(nome_projeto_id=id)

    # projeto_json = json.loads(serializers.serialize('json', projeto))[0]['fields']
    # projeto_id = json.loads(serializers.serialize('json', projeto_json))

    # print(projeto_id)

    # body = json.loads(request.body)
    # id_projeto = get_object_or_404(NovoProjeto, id=id)
    # projeto = NovoProjeto.objects.filter(nome_projeto_id=id_projeto)
    # usuarios = UsuariosProjeto.objects.filter(projeto=projeto[0])
    # projeto_json = json.loads(serializers.serialize('json', projeto))[0]['fields']
    # projeto_id = json.loads(serializers.serialize('json', usuarios))
    # usuarios_json = json.loads(serializers.serialize('json', usuarios))
    # usuarios_json_f = [{'fields': i['fields'], 'id': i['pk']} for i in usuarios_json]
    # lst_usuarios_json = [json.loads(serializers.serialize('json', User.objects.filter(id=usuarioss['fields']['usuario']))) for usuarioss in usuarios_json_f]
    # perfil_usuarios_json = [{'fields': i['fields'], 'perfil': i['pk']} for i in usuarios_json]
    # perfis = [elemento['fields']['perfil'] for elemento in usuarios_json]
    # perfil_usuario_projeto = [json.loads(serializers.serialize('json', PerfilUsuarios.objects.filter(id=perfils['fields']['perfil']))) for perfils in perfil_usuarios_json] 
    # data = {'usuario': lst_usuarios_json, 'projetos': projeto_json, 'projeto_id': projeto_id, 'perfil':perfil_usuario_projeto}



def add_usuarios_projeto(request):
    id_projeto = request.POST.get('id_projeto')
    projeto = NovoProjeto.objects.filter(nome_projeto_id=id_projeto)
    usuarios = UsuariosProjeto.objects.filter(projeto=projeto[0])
    projeto_json = json.loads(serializers.serialize('json', projeto))[0]['fields']
    projeto_id = json.loads(serializers.serialize('json', usuarios))
    usuarios_json = json.loads(serializers.serialize('json', usuarios))
    usuarios_json_f = [{'fields': i['fields'], 'id': i['pk']} for i in usuarios_json]
    lst_usuarios_json = [json.loads(serializers.serialize('json', User.objects.filter(id=usuarioss['fields']['usuario']))) for usuarioss in usuarios_json_f]
    perfil_usuarios_json = [{'fields': i['fields'], 'perfil': i['pk']} for i in usuarios_json]
    perfil_usuario_projeto = [json.loads(serializers.serialize('json', PerfilUsuarios.objects.filter(id=perfils['fields']['perfil']))) for perfils in perfil_usuarios_json] 
    data = {'usuario': lst_usuarios_json, 'projetos': projeto_json, 'projeto_id': projeto_id, 'perfil':perfil_usuario_projeto}
    return JsonResponse(data)
    # return JsonResponse({"teste": 1})






    print(id_projeto)
    # return JsonResponse({'data': 1})
    return JsonResponse(data)





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

    # if status_projeto_filtrar:
    #     projeto = projeto.filter(fase_id=fase_projeto_filtrar)

    

    return render(request, 'projetos.html', {'projeto': projeto,
                                             'status_projeto': status_projeto,
                                             'fase_projeto': fase_projeto})





@login_required(redirect_field_name='login')
def projeto_unico (request, id):
    projeto_unico = get_object_or_404(NovoProjeto, id=id)
    demanda_unica = NovaDemanda.objects.get(id=projeto_unico.nome_projeto_id)
    status = StatusProjeto.objects.all()
    faseprojeto = FaseProjeto.objects.all()
    usuarios_projeto = UsuariosProjeto.objects.filter(projeto_id = id)

    projetos = NovoProjeto.objects.all()

    return render(request, 'projeto_unico.html', {'projeto': projeto_unico,
                                                 'projetos':projetos,
                                                 'status': status,
                                                 'faseprojeto':faseprojeto,
                                                 'demanda_unica': demanda_unica,
                                                 'usuarios_projeto': usuarios_projeto
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

    