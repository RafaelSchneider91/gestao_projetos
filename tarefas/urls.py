from django.urls import path
from . import views

urlpatterns = [
    path('novatarefa/', views.novatarefa, name='novatarefa'),
]