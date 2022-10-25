from django.db import models


class Acompanhamento_animal(models.Model):
    peso = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    altura = models.CharField(max_length=100)
    ficha_clinica = models.URLField(null=True, blank=True)


    def __str__(self):
        return self.peso 

class Raça(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Especie(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Animal(models.Model):
    cruzamento = models.CharField(max_length=100)
    porte = models.CharField(max_length=100)
    especie = models.ForeignKey(Especie, on_delete=models.PROTECT, related_name="animal")
    raca = models.ForeignKey(Raça, on_delete=models.PROTECT, related_name="animal")
    descricao = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    url_foto_animal = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.nome

class doacao(models.Model):
    status = models.CharField(max_length=100)
    data_inicio_doacao = models.CharField(max_length=100)
    data_fim_doacao = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

class adocao(models.Model):
    data_adocao = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome

class Usuario(models.Model):
    cpf = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=13)
    senha = models.CharField(max_length=100)
    confirmacao_senha = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    url_foto_usuario = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.nome