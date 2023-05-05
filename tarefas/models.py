from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
from projetos.models import NovoProjeto, UsuariosProjeto
from datetime import timedelta

class UsuarioTarefa(models.Model):
    usuario_equipe = models.ForeignKey(UsuariosProjeto, on_delete=models.CASCADE)

    def __str__ (self) -> str:
        return self.usuario_equipe


class NovaTarefa(models.Model):
    
    choices_status_tarefa = (
        ('N', 'Não Iniciado'),
        ('E', 'Em andamento'),
        ('P', 'Pendente'),
        ('C', 'Concluido')
    )

    projeto = models.ForeignKey(NovoProjeto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.TextField(max_length=255, blank=False, null=False)
    # membros = models.ForeignKey(UsuariosProjeto, on_delete=models.CASCADE)
    status_tarefa = models.CharField(max_length=50, choices=choices_status_tarefa)
    data_criacao = models.DateTimeField(default = timezone.now)
    data_inicio_planejado = models.DateField(default = timezone.now)
    data_fim_planejado = models.DateField(default = timezone.now() + timedelta(days=10)) #add mais 10 dias caso o campo nao for preenchido;
    data_fim_realizado = models.DateTimeField(null=True, blank=True)

    def __str__ (self) -> str:
        return self.nome
    


    
    