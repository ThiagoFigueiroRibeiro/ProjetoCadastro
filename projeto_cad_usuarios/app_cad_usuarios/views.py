from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse

def home(request):
    
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(nome__contains=str(id_user))
    }
    # Criação da página principal do site.

    return render(request,'usuarios/home.html')

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
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.cep = request.POST.get('cep')
    novo_usuario.bairro = request.POST.get('bairro')
    novo_usuario.n_casa = request.POST.get('n_casa')  
    novo_usuario.telefone = request.POST.get('telefone')   
    novo_usuario.especialidade = request.POST.get('especialidade') 
    novo_usuario.save()

    #Exibir todos os usuarios já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar os dados para a página de listagem dos usuários
    return render(request,'usuarios/usuarios.html', usuarios)
