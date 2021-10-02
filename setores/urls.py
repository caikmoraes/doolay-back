from django.urls import path, include
from rest_framework.routers import DefaultRouter
from setores import views

router = DefaultRouter()
router.register(r'', views.SetorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
