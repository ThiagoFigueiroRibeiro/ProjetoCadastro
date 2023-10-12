from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse

def home(request):
    
    return render(request,'usuarios/home.html')

def cadastro(request):
    
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(nome__contains=str(id_user))
    }
    # Criação da página principal do site.

    return render(request,'usuarios/cadastro.html')

def exibir(request):
    # Exibe todos os usuarios já cadastrados em uma nova página
    usuarios = {'usuarios': Usuario.objects.all()}
    # Retorna os dados para a página de listagem dos usuários
    return render(request,'usuarios/exibir.html', usuarios)

def graph(request):
    # Exibe todos os usuarios já cadastrados em uma nova página
    result_1 = Usuario.objects.filter(especialidade = 'Sem Especialidade').count()
    result_2 = Usuario.objects.filter(especialidade = 'Desportiva').count()
    result_3 = Usuario.objects.filter(especialidade = 'Geriatria').count()
    result_4 = Usuario.objects.filter(especialidade = 'Neuro').count()
    result_5 = Usuario.objects.filter(especialidade = 'Traumato Ortopedia').count()

    context = {
        'result_se': result_1,
        'result_de': result_2,
        'result_ge': result_3,
        'result_ne': result_4,
        'result_to': result_5,
    }
    # Retorna os dados para a página de listagem dos usuários
    return render(request,'usuarios/graph.html', context)

def pesquisa(request):
    # Exibe um usuario específico cadastrado.
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(nome__contains=str(id_user))
    }
    return render(request,'usuarios/pesquisa.html', usuarios)

def counter(request):
    result = Usuario.objects.count()
    return render(request,'usuarios/exibir.html', result)

def view1(request):
    # View 1 logic here
    result1 = "Result from View 1"
    return render(request, 'template1.html', {'result1': result1})

def view2(request):
    # View 2 logic here
    # Call view1 from view2
    result1_from_view2 = view1(request)  # Call view1 like a regular function
    result2 = "Result from View 2"
    return render(request, 'template2.html', {'result1_from_view2': result1_from_view2, 'result2': result2})

def resultado_pesquisa(request):
    # Exibe um usuario específico cadastrado.
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(nome__contains=str(id_user))
    }

    # Exibe o resultado da pesquisa do usuário
    return render(request,'usuarios/resultado_pesquisa.html', usuarios)

def deletar_usuario(request):
    # Deleta um usuario específico da base de dados.
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(id_usuario = id_user).delete()
    }

    # Exibe o resultado da pesquisa do usuário
    return render(request,'usuarios/deletar_usuario.html', usuarios)

def incluir_especialidade(request):
    # Deleta um usuario específico da base de dados.
    id_user = request.POST.get('id_usuario_request')
    spec = request.POST.get('especialidade')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(id_usuario = id_user).update(especialidade=spec)
    }

    # Exibe o resultado da pesquisa do usuário
    return render(request,'usuarios/incluir_especialidade.html', usuarios)

def usuarios(request):
    #Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.save()

    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.cep = request.POST.get('cep')
    novo_usuario.bairro = request.POST.get('bairro')
    novo_usuario.n_casa = request.POST.get('n_casa')  
    novo_usuario.telefone = request.POST.get('telefone')   
    novo_usuario.especialidade = request.POST.get('especialidade') 
    novo_usuario.curso = request.POST.get('curso') 
    novo_usuario.historico = request.POST.get('historico') 
    novo_usuario.info = request.POST.get('info')
          
    novo_usuario.save()

    #Exibir todos os usuarios já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar os dados para a página de listagem dos usuários
    return render(request,'usuarios/usuarios.html', usuarios)

###### Páginas para FISIOTERAPIA  #########

def index_fisio(request):
    return render(request,'usuarios/fisio/index.html')

def exibir_fisio(request):
    # Exibe todos os usuarios já cadastrados em uma nova página
    usuarios = {'usuarios': Usuario.objects.filter(curso = 'Fisioterapia')}
    # Retorna os dados para a página de listagem dos usuários
    return render(request,'usuarios/fisio/exibir.html', usuarios)

def pesquisa_fisio(request):
    # Exibe um usuario específico cadastrado.
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(nome__contains=str(id_user))
    }
    return render(request,'usuarios/fisio/pesquisa.html', usuarios)

def resultado_pesquisa_fisio(request):
    # Exibe um usuario específico cadastrado.
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(nome__contains=str(id_user), curso = 'Fisioterapia')
    }

    # Exibe o resultado da pesquisa do usuário
    return render(request,'usuarios/fisio/resultado_pesquisa.html', usuarios)

def cadastro_fisio(request):
    
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(nome__contains=str(id_user), curso = 'Fisioterapia')
    }
    # Criação da página principal do site.

    return render(request,'usuarios/fisio/cadastro.html')

def usuarios_fisio(request):
    #Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.cep = request.POST.get('cep')
    novo_usuario.bairro = request.POST.get('bairro')
    novo_usuario.n_casa = request.POST.get('n_casa')  
    novo_usuario.telefone = request.POST.get('telefone')   
    novo_usuario.especialidade = request.POST.get('especialidade') 
    novo_usuario.curso = request.POST.get('curso') 
    novo_usuario.historico = request.POST.get('historico') 
    novo_usuario.info = request.POST.get('info')         
    novo_usuario.save()

    #Exibir todos os usuarios já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.filter(curso = 'Fisioterapia')
    }

    # Retornar os dados para a página de listagem dos usuários
    return render(request,'usuarios/fisio/usuarios.html', usuarios)


######## EDUCAÇÃO FÍSICA ############


def index_edfisica(request):
    return render(request,'usuarios/edfisica/index.html')

def exibir_edfisica(request):
    # Exibe todos os usuarios já cadastrados em uma nova página
    usuarios = {'usuarios': Usuario.objects.filter(curso = 'Educação Física')}
    # Retorna os dados para a página de listagem dos usuários
    return render(request,'usuarios/edfisica/exibir.html', usuarios)

def resultado_pesquisa_edfisica(request):
    # Exibe um usuario específico cadastrado.
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(nome__contains=str(id_user), curso = 'Educação Física')
    }

    # Exibe o resultado da pesquisa do usuário
    return render(request,'usuarios/edfisica/resultado_pesquisa.html', usuarios)

def pesquisa_edfisica(request):
    # Exibe um usuario específico cadastrado.
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(nome__contains=str(id_user), curso = 'Educação Física')
    }
    return render(request,'usuarios/edfisica/pesquisa.html', usuarios)

def cadastro_edfisica(request):
    
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(nome__contains=str(id_user))
    }
    # Criação da página principal do site.

    return render(request,'usuarios/edfisica/cadastro.html')

def usuarios_edfisica(request):
    #Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.cep = request.POST.get('cep')
    novo_usuario.bairro = request.POST.get('bairro')
    novo_usuario.n_casa = request.POST.get('n_casa')  
    novo_usuario.telefone = request.POST.get('telefone')   
    novo_usuario.especialidade = request.POST.get('especialidade') 
    novo_usuario.curso = request.POST.get('curso') 
    novo_usuario.historico = request.POST.get('historico') 
    novo_usuario.info = request.POST.get('info')         
    novo_usuario.save()

    #Exibir todos os usuarios já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.filter(curso = 'Educação Física')
    }

    # Retornar os dados para a página de listagem dos usuários
    return render(request,'usuarios/edfisica/usuarios.html', usuarios)



###### NUTRIÇÃO #######


def index_nutri(request):
    return render(request,'usuarios/nutri/index.html')

def exibir_nutri(request):
    # Exibe todos os usuarios já cadastrados em uma nova página
    usuarios = {'usuarios': Usuario.objects.filter(curso = 'Nutrição')}
    # Retorna os dados para a página de listagem dos usuários
    return render(request,'usuarios/nutri/exibir.html', usuarios)

def resultado_pesquisa_nutri(request):
    # Exibe um usuario específico cadastrado.
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(nome__contains=str(id_user), curso = 'Nutrição')
    }

    # Exibe o resultado da pesquisa do usuário
    return render(request,'usuarios/nutri/resultado_pesquisa.html', usuarios)

def pesquisa_nutri(request):
    # Exibe um usuario específico cadastrado.
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(nome__contains=str(id_user), curso = 'Nutrição')
    }
    return render(request,'usuarios/nutri/pesquisa.html', usuarios)

def cadastro_nutri(request):
    
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(nome__contains=str(id_user))
    }
    # Criação da página principal do site.

    return render(request,'usuarios/nutri/cadastro.html')

def usuarios_nutri(request):
    #Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()       
    novo_usuario.save()

    novo_usuario.curso = request.POST.get('curso') 

    novo_usuario.NUTRI_data_avaliacao = request.POST.get('NUTRI_data_avaliacao')
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.data_de_nasc = request.POST.get('data_de_nasc')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.telefone = request.POST.get('telefone')
    novo_usuario.profissao = request.POST.get('profissao')
    novo_usuario.NUTRI_objetivo_da_orientacao = request.POST.get('NUTRI_objetivo_da_orientacao')
    novo_usuario.NUTRI_patologia = request.POST.get('NUTRI_patologia')
    novo_usuario.NUTRI_antecedentes = request.POST.get('NUTRI_antecedentes')
    novo_usuario.NUTRI_atividades = request.POST.get('NUTRI_atividades')
    novo_usuario.NUTRI_atividades_vezes_por_semana = request.POST.get('NUTRI_atividades_vezes_por_semana')
    novo_usuario.NUTRI_ingestao_agua = request.POST.get('NUTRI_ingestao_agua')
    novo_usuario.NUTRI_alergia = request.POST.get('NUTRI_alergia')
    novo_usuario.NUTRI_cafe = request.POST.get('NUTRI_cafe')
    novo_usuario.NUTRI_lanche_manha = request.POST.get('NUTRI_lanche_manha')
    novo_usuario.NUTRI_almoco = request.POST.get('NUTRI_almoco')
    novo_usuario.NUTRI_lanche_tarde = request.POST.get('NUTRI_lanche_tarde')
    novo_usuario.NUTRI_jantar = request.POST.get('NUTRI_jantar')
    novo_usuario.NUTRI_ceia = request.POST.get('NUTRI_ceia')
    
    novo_usuario.NUTRI_CC = request.POST.get('NUTRI_CC')
    novo_usuario.NUTRI_CQ = request.POST.get('NUTRI_CQ')
    novo_usuario.NUTRI_CB = request.POST.get('NUTRI_CB')
    novo_usuario.NUTRI_PCT = request.POST.get('NUTRI_PCT')
    novo_usuario.NUTRI_PCB = request.POST.get('NUTRI_PCB')
    novo_usuario.NUTRI_PCSE = request.POST.get('NUTRI_PCSE')
    novo_usuario.NUTRI_PCSI = request.POST.get('NUTRI_PCSI')
    novo_usuario.NUTRI_gordura = request.POST.get('NUTRI_gordura')
    novo_usuario.NUTRI_massa = request.POST.get('NUTRI_massa')
    novo_usuario.NUTRI_idade_metab = request.POST.get('NUTRI_idade_metab')
    novo_usuario.NUTRI_gordura_visc = request.POST.get('NUTRI_gordura_visc')
    
    novo_usuario.save()

    #Exibir todos os usuarios já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.filter(curso = 'Nutrição')
    }

    # Retornar os dados para a página de listagem dos usuários
    return render(request,'usuarios/nutri/usuarios.html', usuarios)





def index_psico(request):
    return render(request,'usuarios/psico/index.html')

def exibir_psico(request):
    # Exibe todos os usuarios já cadastrados em uma nova página
    usuarios = {'usuarios': Usuario.objects.filter(curso = 'Psicologia')}
    # Retorna os dados para a página de listagem dos usuários
    return render(request,'usuarios/psico/exibir.html', usuarios)

def resultado_pesquisa_psico(request):
    # Exibe um usuario específico cadastrado.
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(nome__contains=str(id_user), curso = 'Psicologia')
    }

    # Exibe o resultado da pesquisa do usuário
    return render(request,'usuarios/psico/resultado_pesquisa.html', usuarios)

def pesquisa_psico(request):
    # Exibe um usuario específico cadastrado.
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(nome__contains=str(id_user), curso = 'psicoçãoa')
    }
    return render(request,'usuarios/psico/pesquisa.html', usuarios)

def cadastro_psico(request):
    
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(nome__contains=str(id_user))
    }
    # Criação da página principal do site.

    return render(request,'usuarios/psico/cadastro.html')

def usuarios_psico(request):
    #Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.cep = request.POST.get('cep')
    novo_usuario.bairro = request.POST.get('bairro')
    novo_usuario.n_casa = request.POST.get('n_casa')  
    novo_usuario.telefone = request.POST.get('telefone')   
    novo_usuario.especialidade = request.POST.get('especialidade') 
    novo_usuario.curso = request.POST.get('curso') 
    novo_usuario.historico = request.POST.get('historico') 
    novo_usuario.info = request.POST.get('info')         
    novo_usuario.save()

    #Exibir todos os usuarios já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.filter(curso = 'Psicologia')
    }

    # Retornar os dados para a página de listagem dos usuários
    return render(request,'usuarios/psico/usuarios.html', usuarios)