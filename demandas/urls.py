from django.urls import path
from . import views

urlpatterns = [
    path('demandas_projeto/', views.demandas_projeto, name='demandas_projeto'),
    path('cadastro_novademanda/', views.cadastro_novademanda, name='cadastro_novademanda'),
    path('<int:iddemanda>', views.demanda_unico, name='demanda_unico'),
    # path('demandas/demanda/<int:iddemanda>', views.demanda_unico, name='demanda_unico'),

    path('', views.demandas, name='demandas'),
    # path('demandas/', views.demandas, name='demandas'),
    path('requisitos/<int:iddemanda>', views.requisitos, name='requisitos'),
    # path('', views.demandas, name='demandas'),
    path('alterastatus/<int:parametro>' , views.alterastatus, name='alterastatus'),

]