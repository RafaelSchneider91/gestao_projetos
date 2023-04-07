from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.categoria
    
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

    nome = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.TextField(max_length=255, blank=False, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True)
    data_cadastro = models.DateTimeField(default = timezone.now) #TODO: esta cadastrando 3 hr a mais
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT, null=True)
    nome_solicitante = models.CharField(max_length=255, blank=False, null=True)
    retorno_financeiro = models.DecimalField(max_digits=50, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    base_calculo_retorno = models.TextField(blank=False, null=True)
    retorno_qualitativo = models.TextField( blank=False, null=True)
    link_analise = models.URLField(blank=True, null=True)
    observacao = models.TextField(blank=False, null=True)
    status = models.ForeignKey(StatusBacklog, on_delete=models.PROTECT, null=True, blank=False)
    usuario_criacao = models.ForeignKey(User, null=True, on_delete=models.CASCADE, blank=True) # TODO: verificar forma de buscar o usuario logado no sistema;
    

    
    def __str__(self) -> str:
        return self.nome
    

    



