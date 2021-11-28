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
   path('relatorio/registros_diarios/<str:date_inicio>/<str:date_final>/', saude_views.relatorio_registros_diarios), #a
   path('relatorio/registros_diarios/<str:date_inicio>/<str:date_final>/plot/', saude_views.plot_registros_diarios), #b
   path('relatorio/noks/<str:date_inicio>/<str:date_final>/', saude_views.relatorio_nok_diarios), #c
   path('relatorio/noks/<str:date_inicio>/<str:date_final>/plot/', saude_views.plot_noks_diarios_valor), #d
   path('relatorio/noks/<str:date_inicio>/<str:date_final>/plot/percentage/', saude_views.plot_noks_diarios_percentage), #d
   path('relatorio/registros/setor/<str:date_inicio>/<str:date_final>/', saude_views.relatorio_registros_setor), #e
   path('relatorio/registros/setor/<str:date_inicio>/<str:date_final>/plot/setor/', saude_views.plot_registros_setor), #f
   path('relatorio/registros/setor/nok/<str:date_inicio>/<str:date_final>/', saude_views.relatorio_registros_noks_setor_percentage), #g
   path('relatorio/registros/setor/nok/<str:date_inicio>/<str:date_final>/plot/setor/<int:pk_setor>/', saude_views.plot_registros_noks_setor), #h
   path('relatorio/registros/setor/nok/<str:date_inicio>/<str:date_final>/plot/setor/<int:pk_setor>/percentage/', saude_views.plot_registros_noks_setor_percentage), #h
   path('relatorio/noks/', saude_views.relatorio_nok_cinco_dias), #i
   path('relatorio/noks/setor/', saude_views.relatorio_nok_cinco_dias_setor), #j
   path('relatorio/registros_minimos/<str:date_inicio>/<str:date_final>/minimo/<int:minimo>/', saude_views.check_attendence), 
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]