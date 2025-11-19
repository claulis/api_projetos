from rest_framework import viewsets
from .models import Projeto, Tarefa, Responsavel
from .serializers import ProjetoSerializer, TarefaSerializer, ResponsavelSerializer

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all().select_related('projeto', 'responsavel')
    serializer_class = TarefaSerializer

class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer