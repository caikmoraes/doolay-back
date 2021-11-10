from django.urls import path
from saude import views as saude_views

urlpatterns = [
    path("listasintomas/", saude_views.ListaSintomasList.as_view()),
    path("listasintomas/<int:pk>/", saude_views.ListaSintomasList.as_view()),
    path("estadosaude/", saude_views.EstadoSaudeList.as_view()),
    path("estadosaude/user/<int:pk>", saude_views.EstadoSaudePerUser.as_view()),
    path("estadosaude/<int:pk>/", saude_views.EstadoSaudeDetail)
]