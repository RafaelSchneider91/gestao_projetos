from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='login')
def novatarefa(request):
    return HttpResponse('em dev')



#TODO: verificar como criar o envio de email para os planos de comunicação.