from django.urls import path
from . import views

urlpatterns = [
    path('', views.projetos, name='projetos'),
    # path('index/', views.index, name='index'),
    # path('novo_demanda/', views.novo_demanda, name='novo_demanda'),
    path('cronograma/', views.cronograma, name='cronograma'),
    path('recurso/', views.recurso, name='recurso'),
    path('painel/', views.painel, name='painel'),
    path('resultado/', views.resultado, name='resultado'),
    # path('admin/', views.admin, name='admin'),
    # path('cadastro_novademanda/', views.cadastro_novademanda, name='cadastro_novademanda'),
    # path('processa_cadastro_novoprojeto/', views.processa_cadastro_novoprojeto, name='processa_cadastro_novoprojeto'),
    path('novo_projeto/', views.novo_projeto, name='novo_projeto'),
]