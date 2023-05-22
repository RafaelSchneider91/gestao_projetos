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
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.conf import settings
from demandas.models import NovaDemanda
from tarefas.models import NovaTarefa
from projetos.models import StatusProjeto, FaseProjeto, NovoProjeto, PerfilUsuarios, UsuariosProjeto, Emails


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
        messages.add_message(request, constants.ERROR, 'Projeto não cadastrado! Verifique os parametros digitados!' )
        return redirect('novo_projeto')
                        
    
    except:
        
        messages.add_message(request, constants.SUCCESS, 'Projeto cadastrado com sucesso!')
        return redirect('novo_projeto')  


@login_required(redirect_field_name='login')
def envia_email(request, id_projeto):
    if request.method == 'POST':
        projeto_unico = NovoProjeto.objects.get(id=id_projeto)
        usuarios_projeto = UsuariosProjeto.objects.filter(recebe_email=1, projeto_id=id_projeto)
        # usuarios = User.objects.filter(id=4)

        ids_usuarios_projeto = usuarios_projeto.values_list('usuario_id', flat=True)

        usuarios = User.objects.filter(id__in=ids_usuarios_projeto)



        # print(usuarios)
        #TODO: fazer validacao se o projeto selecionado possui algum usuario que recebe email;

        # for usuarioa in usuarios_projeto:
        #     print(usuarioa.usuario_id)

        email_usuarios = [usuario.email for usuario in usuarios]
        usuario = [usuario.first_name for usuario in usuarios]


        # if email_usuarios == '':
        #     messages.add_message(request, constants.ERROR, 'Projeto não possui usuarios que recebem email!')
        #     return redirect(f'/projeto/{id_projeto}')

             
        

        
        assunto = request.POST.get('assunto')
        corpo = request.POST.get('corpo')

        contexto = {'usuario': usuario, 
                    'projeto_unico': projeto_unico,
                    'corpo': corpo
                    }
        

        html_content = render_to_string('emails/report_projeto.html',
                                        contexto
                                        )
        
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(assunto, 
                                    text_content, 
                                    settings.EMAIL_HOST_USER,
                                    email_usuarios,
                                    )
        
        email.attach_alternative(html_content, "text/html")

        email.send()



        if len(email_usuarios) == 0:
            messages.add_message(request, constants.ERROR, 'Projeto não possui usuarios que recebem email!')
            return redirect(f'/projeto/{id_projeto}') 

        elif email.send():
            mail = Emails(
                projeto=projeto_unico,
                assunto=assunto,
                corpo=corpo,
                enviado=True
            )
            mail.save()
            messages.add_message(request, constants.SUCCESS, 'Email enviado com sucesso.')
            return redirect(f'/projeto/{id_projeto}')    
                
        
        else:
            mail = Emails(
                projeto=projeto_unico,
                assunto=assunto,
                corpo=corpo,
                enviado=False
            )
            mail.save()
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema!')
            return redirect(f'/projeto/{id_projeto}') 
                

@login_required(redirect_field_name='login')
def add_usuarios_projeto(request):
    if request.method == 'GET':
        usuarios = User.objects.all()
        perfil = PerfilUsuarios.objects.all()
        usuarios_json = json.loads(serializers.serialize('json', usuarios))
        perfil_json = json.loads(serializers.serialize('json', perfil))
        usuarios_json_f = [{'user': i['fields'], 'id': i['pk']} for i in usuarios_json]
        perfil_json_f = [{'perfil': i['fields'], 'id': i['pk']} for i in perfil_json]




        # for a in usuarios:
        #     print(a.id)

        # print(perfil_json)
      
        return JsonResponse({'usuarios': usuarios_json_f,
                             'perfil': perfil_json_f
                             })


#     id_projeto = request.POST.get('id_projeto')
#     projeto = NovoProjeto.objects.filter(nome_projeto_id=id_projeto)
#     usuarios = UsuariosProjeto.objects.filter(projeto=projeto[0])
#     projeto_json = json.loads(serializers.serialize('json', projeto))[0]['fields']
#     projeto_id = json.loads(serializers.serialize('json', usuarios))
#     usuarios_json = json.loads(serializers.serialize('json', usuarios))
#     usuarios_json_f = [{'fields': i['fields'], 'id': i['pk']} for i in usuarios_json]
#     lst_usuarios_json = [json.loads(serializers.serialize('json', User.objects.filter(id=usuarioss['fields']['usuario']))) for usuarioss in usuarios_json_f]
#     perfil_usuarios_json = [{'fields': i['fields'], 'perfil': i['pk']} for i in usuarios_json]
#     perfil_usuario_projeto = [json.loads(serializers.serialize('json', PerfilUsuarios.objects.filter(id=perfils['fields']['perfil']))) for perfils in perfil_usuarios_json] 
#     data = {'usuario': lst_usuarios_json, 'projetos': projeto_json, 'projeto_id': projeto_id, 'perfil':perfil_usuario_projeto}
    
    elif request.method == "POST":
    
        pass


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
    total_tarefas = NovaTarefa.objects.filter(projeto_id = id).count()
    total_tarefas_nao_concluidas = NovaTarefa.objects.filter(projeto_id = id, status_tarefa='C').count()

    if total_tarefas_nao_concluidas != 0:
        percentual_projeto = round(((total_tarefas_nao_concluidas/total_tarefas)*100))
    else:
        percentual_projeto = 0
    

    # print(percentual_projeto)
    
    usuarios_projeto = UsuariosProjeto.objects.filter(projeto_id = id)

    for usuario_projeto in usuarios_projeto:
   
        user = usuario_projeto.usuario

        username = user.username
        email = user.email
        # print(username, email)

            
    projetos = NovoProjeto.objects.all()

    contexto = {'projeto': projeto_unico,
                'projetos':projetos,
                'status': status,
                'faseprojeto':faseprojeto,
                'demanda_unica': demanda_unica,
                'usuarios_projeto': usuarios_projeto,
                'percentual_projeto': percentual_projeto
                }

    return render(request, 'projeto_unico.html', contexto)

@login_required(redirect_field_name='login')
def updateprojeto(request, id):
    if request.method == 'POST':
        descricao_projeto = request.POST.get('descricao_projeto')
        status_projeto = request.POST.get('status_projeto')
        fase_projeto = request.POST.get('fase_projeto')
        prioridade_projeto = request.POST.get('prioridade_projeto')

        nome_projeto = NovoProjeto.objects.filter(id=id)

        nome_id = [nome.nome_projeto_id for nome in nome_projeto]

        u_projetos = NovoProjeto(
            id = id,
            nome_projeto_id = nome_id[0], #pega o primeiro elemento da lista
            descricao_projeto = descricao_projeto,
            status_id = status_projeto,
            fase_id = fase_projeto,
            prioridade = prioridade_projeto,

        )
        u_projetos.save()

        return redirect('projetos')