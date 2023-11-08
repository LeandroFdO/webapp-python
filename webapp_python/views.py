from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import produtos

# Create your views here.

def home(request):
    return render(request, "menu/home.html")

def results(request):
    novo_produto = produtos()
    novo_produto.nome = request.POST.get('nome')
    novo_produto.valor = request.POST.get('valor')
    novo_produto.tipo = request.POST.get('tipo')
    novo_produto.fornecedor = request.POST.get('fornecedor')
    novo_produto.quantidade = request.POST.get('quantidade')
    novo_produto.save()
    return render(request, 'menu/sucess.html')

def sucess(request):
    return render(request, "menu/home.html")

def consulta(request):
    tabela = produtos.objects.all()
    return render(request, 'menu/consulta.html', {'produtos': tabela})
