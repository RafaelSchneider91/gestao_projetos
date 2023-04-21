from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from projetos.models import NovoProjeto

@login_required(redirect_field_name='login')
def tarefa(request, id):
    projeto_unico = get_object_or_404(NovoProjeto, id=id)


    projetos = NovoProjeto.objects.all()


    return render(request,'tarefa.html', {'projetos': projetos,
                                          'projeto': projeto_unico})


@login_required(redirect_field_name='login')
def novatarefa(request):    
    return HttpResponse('em dev')






#TODO: verificar como criar o envio de email para os planos de comunicação.