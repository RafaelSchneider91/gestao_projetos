from django.contrib import admin
from .models import Setor, NovaDemanda, StatusBacklog, Requisitos, UserStories, PrioridadeUserStorie

admin.site.register(Setor)
admin.site.register(StatusBacklog)

admin.site.register(PrioridadeUserStorie)
admin.site.register(UserStories)

class NovaDemandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_cadastro','usuario_criacao','setor_demanda')

admin.site.register(NovaDemanda, NovaDemandaAdmin)

class RequisitoAdmin(admin.ModelAdmin):
    list_display = ('demanda', 'id_demanda_requisito', 'descricao_requisito')

admin.site.register(Requisitos, RequisitoAdmin)




