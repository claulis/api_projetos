from rest_framework import serializers
from .models import Projeto, Tarefa, Responsavel

class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = '__all__'

class TarefaSerializer(serializers.ModelSerializer):
    projeto = serializers.PrimaryKeyRelatedField(queryset=Projeto.objects.all())
    responsavel = serializers.PrimaryKeyRelatedField(queryset=Responsavel.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Tarefa
        fields = '__all__'

class ProjetoSerializer(serializers.ModelSerializer):
    tarefas = TarefaSerializer(many=True, read_only=True)  # opcional: mostra tarefas dentro do projeto

    class Meta:
        model = Projeto
        fields = '__all__'