from django.contrib import admin
from projetos.models import StatusProjeto, NovoProjeto, FaseProjeto, PerfilUsuarios, UsuariosProjeto, Emails

admin.site.register(StatusProjeto)
admin.site.register(FaseProjeto)
admin.site.register(PerfilUsuarios)


class UsuariosProjetoAdmin(admin.ModelAdmin):
    list_display = ('projeto', 'usuario', 'perfil', 'recebe_email')
    list_filter = (['projeto', 'usuario'])

class NovoProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome_projeto', 'categoria', 'data_cadastro', 'status')
    list_filter = (['nome_projeto', 'data_cadastro'])

class EmailsAdmin(admin.ModelAdmin):
    list_display = ('projeto','assunto')



admin.site.register(UsuariosProjeto, UsuariosProjetoAdmin)
admin.site.register(NovoProjeto, NovoProjetoAdmin)
admin.site.register(Emails, EmailsAdmin)





# Register your models here.
