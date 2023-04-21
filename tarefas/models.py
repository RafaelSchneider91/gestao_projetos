from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from projetos.models import NovoProjeto

class NovaTarefa(models.Model):
    
    choices_status_tarefa = (
        ('N', 'Não Iniciado'),
        ('E', 'Em andamento'),
        ('C', 'Concluido')
    )


    nome = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.TextField(max_length=255, blank=False, null=False)
    membros = models.ManyToManyField(User)
    status_tarefa = models.CharField(max_length=50, choices=choices_status_tarefa)
    data_criacao = models.DateTimeField(default = timezone.now) #TODO: esta cadastrando 3 hr a mais
    data_inicio_planejado = models.DateField(default = timezone.now)
    data_fim_planejado = models.DateField(default = timezone.now)
    data_fim_realizado = models.DateTimeField(default = timezone.now)
    projeto = models.ForeignKey(NovoProjeto, on_delete=models.CASCADE)

    def __str__ (self) -> str:
        return self.nome


    
    