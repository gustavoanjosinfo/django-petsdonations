from django.db import models

class Espécie(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Raça(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome