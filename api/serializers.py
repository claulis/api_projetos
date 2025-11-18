from rest_framework import serializers
from .models import Projeto, Tarefa, Responsavel

class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = ['id', 'nome', 'email']

class TarefaSerializer(serializers.ModelSerializer):
    responsaveis = ResponsavelSerializer(many=True, read_only=True)

    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'concluida', 'responsaveis']

class ProjetoSerializer(serializers.ModelSerializer):
    tarefas = TarefaSerializer(many=True, read_only=True)

    class Meta:
        model = Projeto
        fields = ['id', 'nome', 'descricao', 'data_inicio', 'tarefas']