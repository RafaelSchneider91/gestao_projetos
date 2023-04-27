from django.contrib import admin
from projetos.models import StatusProjeto, NovoProjeto, FaseProjeto, PerfilUsuarios, UsuariosProjeto

admin.site.register(StatusProjeto)
admin.site.register(FaseProjeto)
admin.site.register(NovoProjeto)
admin.site.register(PerfilUsuarios)


class UsuariosProjetoAdmin(admin.ModelAdmin):
    list_display = ('projeto', 'usuario', 'perfil')

admin.site.register(UsuariosProjeto, UsuariosProjetoAdmin)





# Register your models here.
