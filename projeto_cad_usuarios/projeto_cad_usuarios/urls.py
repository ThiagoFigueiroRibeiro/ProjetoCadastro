from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # usuarios.com
    path('',views.home,name='home'),

    path('cadastro/',views.cadastro,name='cadastro'),

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

    # usuarios.com/incluir_especialidade - Para incluir a especialidade a um usuário.
    path('incluir_especialidade/',views.incluir_especialidade,name='incluir_especialidade'),

    # usuarios.com/incluir_especialidade - Para incluir a especialidade a um usuário.
    path('graph/',views.graph,name='graph'),
    
    ######## FISIOTERAPIA ###########
    path('fisio/index/',views.index_fisio,name='home_fisio'),
    path('fisio/exibir/',views.exibir_fisio,name='exibir_fisio'),
    path('fisio/resultado_pesquisa/',views.resultado_pesquisa_fisio,name='resultado_pesquisa_fisio'),
    path('fisio/pesquisa/',views.pesquisa_fisio,name='pesquisa_usuarios_fisio'),
    path('fisio/cadastro/',views.cadastro_fisio,name='cadastro_fisio'),
    path('fisio/usuarios/',views.usuarios_fisio,name='listagem_usuarios_fisio'),

        ######## EDUCAÇÃO FÍSICA ###########
    path('edfisica/index/',views.index_edfisica,name='home_edfisica'),
    path('edfisica/exibir/',views.exibir_edfisica,name='exibir_edfisica'),
    path('edfisica/resultado_pesquisa/',views.resultado_pesquisa_edfisica,name='resultado_pesquisa_edfisica'),
    path('edfisica/pesquisa/',views.pesquisa_edfisica,name='pesquisa_usuarios_edfisica'),
    path('edfisica/cadastro/',views.cadastro_edfisica,name='cadastro_edfisica'),
    path('edfisica/usuarios/',views.usuarios_edfisica,name='listagem_usuarios_edfisica'),
]
