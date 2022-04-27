from django.shortcuts import render


def index(request):
    return render(request, 'postagens-resumo.html', {})

def postagem(request):
    return render(request, 'postagens.html', {})

def comentarios_sugestoes(request):
    return render(request,'comentarios_sugestoes.html', {})

def sobre(request):
    return render(request, 'sobre.html', {})

def inscreva_se(request):
    return render(request,'inscreva-se.html', {})

def atividades(request):
    return render(request,'atividades.html', {})

def login(request):
    return render(request, 'login.html', {})