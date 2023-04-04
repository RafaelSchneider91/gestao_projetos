from django.db import models

class NovaDemanda(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    descricao = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.nome
