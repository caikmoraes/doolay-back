from django.urls import path, re_path, include
from saude import views as saude_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="Test description",
   )
)

router = DefaultRouter()
router.register(r'estadosaude', saude_views.EstadoSaudeViewSet)
router.register(r'sintomas', saude_views.SintomaViewSet)
router.register(r'item_sintoma', saude_views.EstadoItemSintomaViewSet)
router.register(r'listasintomas', saude_views.ListaSintomasViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('estadosaude/user/<str:user_pk>/', saude_views.EstadoSaudeDetail.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]