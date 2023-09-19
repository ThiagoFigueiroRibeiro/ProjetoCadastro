from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    cep = models.TextField(max_length=255)
    bairro = models.TextField(max_length=255)
    n_casa = models.IntegerField()
    telefone = models.IntegerField()
    especialidade = models.TextField(blank=True)