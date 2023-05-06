from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from projetos.models import NovoProjeto
from tarefas.models import NovaTarefa
from django.contrib import messages
from django.contrib.messages import constants
from django.core import serializers
import json



@login_required(redirect_field_name='login')
def tarefas(request):
    if request.method == "GET":


        projetos = NovoProjeto.objects.all()
        # tarefas = NovaTarefa.objects.filter(id=id)
        # print(tarefas)
        
        return render(request, 'tarefas.html', {'projetos': projetos})




    elif request.method == "POST":
        projeto_id = request.POST.get('projeto')
        nome_tarefa = request.POST.get('titulo')
        descricao_tarefa = request.POST.get('descricao_tarefa')
        status_tarefa = request.POST.get('status_tarefa')
        data_plan_inicio = request.POST.get('data_inicio_plan')
        data_plan_fim = request.POST.get('data_fim_plan')


        tarefa = NovaTarefa(projeto_id = projeto_id,
                            nome = nome_tarefa,
                            descricao = descricao_tarefa,
                            status_tarefa = status_tarefa,
                            data_inicio_planejado = data_plan_inicio,
                            data_fim_planejado = data_plan_fim
        )

    
    try:
        tarefa.save()
        # messages.add_message(request, constants.SUCCESS, 'Tarefa cadastrada com sucesso!')
        return redirect('tarefas')

    except:
        # messages.add_message(request, constants.ERROR, 'Tarefa não cadastrada! Verifique os parametros digitados!' )
        return redirect('tarefas')

@login_required(redirect_field_name='login')
def tarefa_unica(request, id):
    tarefa_unica = get_object_or_404(NovaTarefa, id=id)
    print(tarefa_unica)




    return render(request, 'modal_tarefa_unica.html', {'tarefa': tarefa_unica})


@login_required(redirect_field_name='login')
def alteraprojeto(request):

    if request.method == "POST":
        id_projeto = request.POST.get('id_projeto')
        tarefas = NovaTarefa.objects.filter(projeto_id=id_projeto)
        tarefas_json = serializers.serialize('json', tarefas)
        tarefas_json_json = json.loads(tarefas_json)

        # print(type(tarefas_json))
        # print(tarefas_json_json)

        # tarefas_data = []
        # for tarefa_data in tarefas_json_json:
        #     tarefa_fields = tarefa_data['fields']
        #     tarefas_data.append(tarefa_fields)

    tarefas_json_f = [{'fields': tarefa['fields'], 'id_tarefa':tarefa['pk']} for tarefa in tarefas_json_json]
            # print(tarefa_fields['nome'])
            # print(tarefa_fields['descricao'])
            # print(tarefa_fields['data_de_criacao'])

        # print(tarefas_data)
    # print(tarefas_json_f)

    # return JsonResponse(tarefa_data)
    return JsonResponse({'tarefas': tarefas_json_f})
    # return JsonResponse({'teste':1})  


#TODO: verificar como criar o envio de email para os planos de comunicação.


# @login_required(redirect_field_name='login')
# def novatarefa(request):
#     if request.method == "GET":
#         return HttpResponse('em dev')




#     elif request.method == "POST":
#         projeto_id = request.POST.get('projeto')
#         nome_tarefa = request.POST.get('titulo')
#         descricao_tarefa = request.POST.get('descricao_tarefa')
#         status_tarefa = request.POST.get('status_tarefa')
#         data_plan_inicio = request.POST.get('data_inicio_plan')
#         data_plan_fim = request.POST.get('data_fim_plan')


#         tarefa = NovaTarefa(projeto_id = projeto_id,
#                             nome = nome_tarefa,
#                             descricao = descricao_tarefa,
#                             status_tarefa = status_tarefa,
#                             data_inicio_planejado = data_plan_inicio,
#                             data_fim_planejado = data_plan_fim
#         )

    
#     try:
#         tarefa.save()
#         messages.add_message(request, constants.SUCCESS, 'Tarefa cadastrada com sucesso!')
#         return redirect('tarefas')

#     except:
#         messages.add_message(request, constants.ERROR, 'Tarefa não cadastrada! Verifique os parametros digitados!' )
#         return redirect('tarefas')