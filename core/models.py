from django.db import models

class Acompanhamento_animal(models.Model):
    peso = models.CharField(max_length=100)
    id_acompanhamento = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    altura = models.CharField(max_length=100)
    ficha_clinica = models.URLField(null=True, blank=True)


    def __str__(self):
        return self.peso 

class Raça(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome