from django.urls import path
from . import views

urlpatterns = [
    path('demandas_projeto/', views.demandas_projeto, name='demandas_projeto'),
    path('cadastro_novademanda/', views.cadastro_novademanda, name='cadastro_novademanda'),
    path('demanda/<int:id>', views.demanda_unico, name='demanda_unico'),
    path('demandas/', views.demandas, name='demandas'),
    # path('processa_cadastro_novademanda/', views.processa_cadastro_novademanda, name='processa_cadastro_novademanda'),
]