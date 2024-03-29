from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

  
class Setor(models.Model):
    setor = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.setor
    
    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'


class StatusBacklog(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.status

    

class NovaDemanda(models.Model):

    nome = models.CharField(max_length=50, blank=False, null=False)
    descricao = models.TextField(max_length=255, blank=False, null=False)
    data_cadastro = models.DateTimeField(default = timezone.now)
    setor_demanda = models.ForeignKey(Setor, on_delete=models.CASCADE)
    nome_solicitante = models.CharField(max_length=255, blank=False, null=False)
    retorno_financeiro = models.DecimalField(max_digits=50, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    base_calculo_retorno = models.TextField(blank=False, null=False)
    retorno_qualitativo = models.TextField( blank=False, null=False)
    link_analise = models.URLField(blank=True, null=True)
    observacao = models.TextField(blank=False, null=True)
    status_backlog = models.ForeignKey(StatusBacklog, on_delete=models.CASCADE)
    usuario_criacao = models.ForeignKey(User, on_delete=models.CASCADE) # TODO: verificar forma de buscar o usuario logado no sistema;
    

    
    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        verbose_name = 'Demanda'



