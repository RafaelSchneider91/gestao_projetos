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
    data_cadastro = models.DateTimeField(default = timezone.now)
    staramais = models.BooleanField(default=False)
    staralabs = models.BooleanField(default=False)
    prioridade = models.PositiveIntegerField(default=1000)
    # membros = models.ManyToManyField(User, null=True, on_delete=models.CASCADE)
    # equipe = models.ManyToManyField(User)

    def __str__ (self) -> str:
        return self.nome_projeto.nome
    
    class Meta:
        verbose_name = 'Projeto'
    
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

    

    def __int__(self) -> int:
        return self.projeto
    

class Emails(models.Model):
    projeto = models.ForeignKey(NovoProjeto, on_delete=models.DO_NOTHING)
    assunto = models.CharField(max_length=100)
    corpo = models.TextField()
    enviado = models.BooleanField()
    data_cadastro = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.assunto
    
    class Meta:
        verbose_name = 'Emails Enviado'

class Ata(models.Model):

    choices_categoria = (
        ('I', 'Informação'),
        ('P', 'Pendência'),
        ('O', 'Outros')
    )

    projeto = models.ForeignKey(NovoProjeto, on_delete=models.CASCADE)
    data_hora_reunião = models.DateTimeField(default = timezone.now)
    assunto = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=choices_categoria, default='M')
    local = models.CharField(max_length=100)
    participantes = models.ForeignKey(UsuariosProjeto, on_delete=models.CASCADE)
    distribuido = models.ForeignKey(UsuariosProjeto, on_delete=models.CASCADE, related_name='distribuido')
    atividadeouassunto = models.TextField()
    quem = models.ForeignKey(UsuariosProjeto, on_delete=models.CASCADE, related_name='quem')
    quando = models.DateField(null=True, blank=True)
    data_cadastro = models.DateTimeField(default = timezone.now)

    





