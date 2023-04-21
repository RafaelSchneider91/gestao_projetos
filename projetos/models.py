from django.db import models
from django.contrib.auth.models import User
from demandas.models import NovaDemanda
from django.utils import timezone


class StatusProjeto(models.Model):
    status = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.status
    
class FaseProjeto(models.Model):
    fase = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.fase


class NovoProjeto(models.Model):
    nome_projeto = models.ForeignKey(NovaDemanda, null=True, on_delete=models.CASCADE)
    descricao_projeto = models.TextField(blank=False, null=False)
    status = models.ForeignKey(StatusProjeto, on_delete=models.CASCADE, null=True, blank=False)
    fase = models.ForeignKey(FaseProjeto, on_delete=models.CASCADE, null=True, blank=False)
    data_cadastro = models.DateTimeField(default = timezone.now) #TODO: esta cadastrando 3 hr a mais
    staramais = models.BooleanField(default=False)
    staralabs = models.BooleanField(default=False)
    prioridade = models.PositiveIntegerField(default=1000)
    equipe = models.ManyToManyField(User)

    def __str__ (self) -> str:
        return self.nome_projeto.nome
    






