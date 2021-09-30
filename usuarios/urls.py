from django.urls import path, include, re_path
from usuarios.views import AlunosCreate, validate_aluno, AlunosDetail, FuncionarioCreate, FuncionariosDetail, validate_funcionario

urlpatterns = [
    path('alunos/create/', AlunosCreate.as_view()),
    path('alunos/login/', validate_aluno),
    path('alunos/<str:pk>/', AlunosDetail.as_view()),
    path('funcionarios/create/', FuncionarioCreate.as_view()),
    path('funcionarios/login/', validate_funcionario),
    path('funcionarios/<str:pk>/', FuncionariosDetail.as_view())
]
