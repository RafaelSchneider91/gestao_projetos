from django.urls import path
from . import views

urlpatterns = [
    # path('novatarefa/', views.novatarefa, name='nova_tarefa'),
    # path('tarefa/<int:id>', views.tarefa, name='tarefa'),
    path('tarefas/', views.tarefas, name='tarefas'),
    path('', views.tarefas, name='tarefas'),
    path('tarefas/alteraprojeto/', views.alteraprojeto, name='alteraprojeto')
]