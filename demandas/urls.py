from django.urls import path
from . import views

urlpatterns = [
    path('novo_demanda/', views.novo_demanda, name='novo_demanda'),
    path('cadastro_novademanda/', views.cadastro_novademanda, name='cadastro_novademanda'),
    # path('processa_cadastro_novademanda/', views.processa_cadastro_novademanda, name='processa_cadastro_novademanda'),
]