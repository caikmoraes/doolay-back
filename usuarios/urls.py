from django.urls import path, include, re_path
from usuarios.views import AlunosCreate, validate_aluno, AlunosDetail

urlpatterns = [
    path('alunos/create/', AlunosCreate.as_view()),
    path('alunos/login/', validate_aluno),
    path('alunos/<str:pk>/', AlunosDetail.as_view())
]
