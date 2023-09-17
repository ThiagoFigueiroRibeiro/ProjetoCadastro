from django.shortcuts import render
from .models import Usuario

def home(request):
    # Criação da página principal do site.
    return render(request,'usuarios/home.html')

def exibir(request):
    # Exibe todos os usuarios já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retorna os dados para a página de listagem dos usuários
    return render(request,'usuarios/exibir.html', usuarios)

def pesquisa(request):
    # Exibe um usuario específico cadastrado.
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(id_usuario = id_user)
    }

    return render(request,'usuarios/pesquisa.html', usuarios)

def resultado_pesquisa(request):
    # Exibe um usuario específico cadastrado.
    id_user = request.POST.get('id_usuario_request')
    usuarios = {
        'usuarios_filter': Usuario.objects.filter(id_usuario = id_user)
    }

    # Exibe o resultado da pesquisa do usuário
    return render(request,'usuarios/resultado_pesquisa.html', usuarios)


def usuarios(request):
    #Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.peso = request.POST.get('peso')
    novo_usuario.altura = request.POST.get('altura')    
    novo_usuario.save()

    #Exibir todos os usuarios já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar os dados para a página de listagem dos usuários
    return render(request,'usuarios/usuarios.html', usuarios)
