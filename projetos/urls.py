from django.urls import path
from . import views

urlpatterns = [
    path('', views.projetos, name='projetos'),
    path('novo_projeto/', views.novo_projeto, name='novo_projeto'),
    path('projeto/<int:id>', views.projeto_unico, name='projeto_unico'),
    path('editar_projeto/<int:id>/', views.editar_projeto, name='editar_projeto'),
    


    #VERIFICAR
    # path('cronograma/', views.cronograma, name='cronograma'),
    # path('membros/', views.membros, name='membros'),   
    # path('resultado/', views.resultado, name='resultado'),
    
]