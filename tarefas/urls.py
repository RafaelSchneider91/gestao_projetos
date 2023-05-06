from django.urls import path
from . import views

urlpatterns = [
    # path('novatarefa/', views.novatarefa, name='nova_tarefa'),
    # path('tarefa/<int:id>', views.tarefa, name='tarefa'),
    path('tarefas/', views.tarefas, name='tarefas'),
    path('tarefa/<int:id>', views.tarefa_unica, name='tarefa_unica'),
    path('', views.tarefas, name='tarefas'),
    path('tarefas/alteraprojeto/', views.alteraprojeto, name='alteraprojeto')
]