from django.contrib import admin
from tarefas.models import NovaTarefa,UsuarioTarefa


class NovaTarefaAdmin(admin.ModelAdmin):
    list_filter = ('projeto', 'status_tarefa')


admin.site.register(NovaTarefa, NovaTarefaAdmin)
admin.site.register(UsuarioTarefa)