from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login (request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, email=email, password=senha)
    print(user)

    if not user:
        messages.error(request, 'Usuario ou senha invalidos')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        # messages.success(request, 'Voce fez login com sucesso')
        return redirect ('projetos')

def logout (request):
    auth.logout(request)
    return redirect('login')



