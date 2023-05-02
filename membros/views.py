from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from projetos.models import NovoProjeto, PerfilUsuarios, UsuariosProjeto
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages



@login_required(redirect_field_name='login')
def membros(request):
    if request.method == "GET":
        projetos = NovoProjeto.objects.all()
        usuarios = User.objects.all()
        perfil_usuario = PerfilUsuarios.objects.all()




        return render(request, 'membros.html', {'perfil_usuario': perfil_usuario,
                                                'projetos': projetos,
                                                'usuarios': usuarios,
                                                    
                                                    })
    elif request.method == "POST":
        nome_projeto_id = request.POST.get('projeto_id')
        usuario_id = request.POST.get('usuario_id')
        perfil_id = request.POST.get('perfil_id')
               
        if request.POST.get('recebe_email') == None:    
            recebe_email = False
        else:
            recebe_email = True
        
        usuario_projeto = UsuariosProjeto(projeto_id = nome_projeto_id,
                    usuario_id = usuario_id,
                    perfil_id  = perfil_id,
                    recebe_email = recebe_email
        )

        try:
            usuario_projeto.save()
            messages.add_message(request, constants.SUCCESS, 'Usuario cadastrado com sucesso!')
            return redirect('membros')
        except:
            messages.add_message(request, constants.ERROR, 'Usuario não cadastrado! Usuario ja cadastrado!' )
            return redirect('membros')
