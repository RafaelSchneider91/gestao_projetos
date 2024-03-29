from django.urls import path
from . import views

urlpatterns = [
    path('', views.projetos, name='projetos'),
    path('novo_projeto/', views.novo_projeto, name='novo_projeto'),
    path('projeto/<int:id>', views.projeto_unico, name='projeto_unico'),
    # path('editar_projeto/<int:id>/', views.editar_projeto, name='editar_projeto'),
    path('novo_projeto/add_usuarios_projeto/', views.add_usuarios_projeto, name='add_usuarios_projeto'),
    # path('<int:id>/usuarios_projeto/', views.usuarios_projeto, name='usuarios_projeto'),

    path('envia_email/<int:id_projeto>', views.envia_email, name="envia_email"),
    
    path('update/<int:id>', views.updateprojeto, name="updateprojeto")
 
    


    #VERIFICAR
    # path('cronograma/', views.cronograma, name='cronograma'),
    # path('membros/', views.membros, name='membros'),   
    # path('resultado/', views.resultado, name='resultado'),
    
]