from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Responsavel(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tarefas')
    responsavel = models.ForeignKey(Responsavel, on_delete=models.SET_NULL, null=True, blank=True, related_name='tarefas')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.projeto.nome})"