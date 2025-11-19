from rest_framework.routers import DefaultRouter
from .views import ProjetoViewSet, TarefaViewSet, ResponsavelViewSet

router = DefaultRouter()
router.register(r'projetos', ProjetoViewSet, basename='projeto')
router.register(r'tarefas', TarefaViewSet, basename='tarefa')
router.register(r'responsaveis', ResponsavelViewSet, basename='responsavel')

urlpatterns = router.urls