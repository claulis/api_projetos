# api/models.py
from django.db import models

class Projeto(models.Model):
    nome = models.CharField("Nome do Projeto", max_length=200)
    descricao = models.TextField("Descrição", blank=True)
    data_inicio = models.DateField("Data de Início")

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tarefas')
    titulo = models.CharField("Título da Tarefa", max_length=200)
    concluida = models.BooleanField("Concluída", default=False)

    def __str__(self):
        return self.titulo

class Responsavel(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name='responsaveis')
    nome = models.CharField("Nome do Responsável", max_length=100)
    email = models.EmailField("E-mail")

    def __str__(self):
        return self.nome