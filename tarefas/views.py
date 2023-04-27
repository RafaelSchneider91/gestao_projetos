from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from projetos.models import NovoProjeto

@login_required(redirect_field_name='login')
def novatarefa(request):    
    return HttpResponse('em dev')

@login_required(redirect_field_name='login')
def tarefas(request):
    # projeto_unico = get_object_or_404(NovoProjeto, id=id)


    # projetos = NovoProjeto.objects.all()


    return render(request,'tarefas.html')








#TODO: verificar como criar o envio de email para os planos de comunicação.