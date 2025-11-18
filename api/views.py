from rest_framework import viewsets
from .models import Projeto
from .serializers import ProjetoSerializer

#class ProjetoViewSet(viewsets.ModelViewSet):
#    queryset = Projeto.objects.all().prefetch_related('tarefas__responsaveis')
#    serializer_class = ProjetoSerializer

# api/views.py
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all().prefetch_related('tarefas__responsaveis')
    serializer_class = ProjetoSerializer

    # Exemplo de documentação manual (opcional)
    @swagger_auto_schema(
        operation_description="Lista todos os projetos com suas tarefas e responsáveis aninhados",
        responses={200: ProjetoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)