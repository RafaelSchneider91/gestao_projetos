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
    

class NovaDemanda(models.Model):

    choices_categoria = (
        ('M', 'Melhoria'),
        ('P', 'Projeto')
    )
    choices_statusbacklog = (
        ('P', 'Aguardando Priorizacao'),
        ('A', 'Em analise')
    )



    nome = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.TextField(max_length=255, blank=False, null=False)
    categoria = models.CharField(max_length=50, choices=choices_categoria)
    data_cadastro = models.DateTimeField(default = timezone.now) #TODO: esta cadastrando 3 hr a mais
    setor_demanda = models.ForeignKey(Setor, on_delete=models.PROTECT)
    nome_solicitante = models.CharField(max_length=255, blank=False, null=True)
    retorno_financeiro = models.DecimalField(max_digits=50, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    base_calculo_retorno = models.TextField(blank=False, null=True)
    retorno_qualitativo = models.TextField( blank=False, null=True)
    link_analise = models.URLField(blank=True, null=True)
    observacao = models.TextField(blank=False, null=True)
    status = models.CharField(max_length=50, choices=choices_statusbacklog)
    usuario_criacao = models.ForeignKey(User, on_delete=models.PROTECT) # TODO: verificar forma de buscar o usuario logado no sistema;
    

    
    def __str__(self) -> str:
        return self.nome
    

    



