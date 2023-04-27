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
    
class PerfilUsuarios(models.Model):
    perfil = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.perfil

class NovoProjeto(models.Model):
    choices_categoria = (
        ('M', 'Melhoria'),
        ('P', 'Projeto')
    )

    nome_projeto = models.ForeignKey(NovaDemanda, null=True, on_delete=models.CASCADE)
    descricao_projeto = models.TextField(blank=False, null=False)
    status = models.ForeignKey(StatusProjeto, on_delete=models.CASCADE, null=True, blank=False)
    categoria = models.CharField(max_length=50, choices=choices_categoria, default='M')
    fase = models.ForeignKey(FaseProjeto, on_delete=models.CASCADE, null=True, blank=False)
    data_cadastro = models.DateTimeField(default = timezone.now) #TODO: esta cadastrando 3 hr a mais
    staramais = models.BooleanField(default=False)
    staralabs = models.BooleanField(default=False)
    prioridade = models.PositiveIntegerField(default=1000)
    # membros = models.ManyToManyField(User, null=True, on_delete=models.CASCADE)
    # equipe = models.ManyToManyField(User)

    def __str__ (self) -> str:
        return self.nome_projeto.nome
    
class UsuariosProjeto(models.Model):
    projeto = models.ForeignKey(NovoProjeto, null=True, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    perfil = models.ForeignKey(PerfilUsuarios, null=True, on_delete=models.CASCADE)
    recebe_email = models.BooleanField(default=False)

    class Meta:
        constraints = [
            # impede q o mesmo usuario tenha o mesmo conteudo mais que uma vez como favorito
            models.UniqueConstraint(fields=['usuario', 'projeto'], name='fav_user_content')
        ]

    

    # def __str__(self) -> str:
    #     return self.projeto







