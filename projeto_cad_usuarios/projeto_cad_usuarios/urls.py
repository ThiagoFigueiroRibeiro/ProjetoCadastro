from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # usuarios.com
    path('',views.home,name='home'),

    # usuarios.com/usuarios - Quando um usuário novo é cadastrado, essa página é exibida.
    path('usuarios/',views.usuarios,name='listagem_usuarios'),

   # usuarios.com/exibir - Exibe uma lista com todos os usuários cadastrados.
    path('exibir/',views.exibir,name='exibir_usuarios'),

    # usuarios.com/pesquisa - Página de pesquisa específica de usuário.
    path('pesquisa/',views.pesquisa,name='pesquisa_usuarios'),

    # usuarios.com/resultado_pesquisa - Exibe uma lista com os dados de um determinado usuário.
    path('resultado_pesquisa/',views.resultado_pesquisa,name='resultado_pesquisa'),

    # usuarios.com/deletar_usuario - Página que você solicita a exclusão de um usuário.
    path('deletar_usuario/',views.deletar_usuario,name='deletar_usuario'),
]
