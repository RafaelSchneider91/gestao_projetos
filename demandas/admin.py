from django.contrib import admin
from .models import Setor, NovaDemanda, StatusBacklog

admin.site.register(Setor)
admin.site.register(StatusBacklog)

class NovaDemandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_cadastro','usuario_criacao','setor_demanda')

admin.site.register(NovaDemanda, NovaDemandaAdmin)

