from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuração do Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="API Gestão de Projetos",
      default_version='v1',
      description="API REST para gerenciamento de projetos, tarefas e responsáveis",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="seu-email@exemplo.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Nossos endpoints da API
    path('api/', include('api.urls')),
    
    # Swagger UI (bonitão e interativo)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # ReDoc (outra interface mais clean, opcional)
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # Arquivo JSON/YAML da especificação (útil para ferramentas externas)
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]