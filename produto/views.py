from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore
from django.views.generic.list import ListView # type: ignore
from django.views import View # type: ignore
from . import models


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10
    

class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('DetalheProduto')
    

class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('AdicionarAoCarrinho')
    

class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('RemoverDoCarrinho')
    

class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')
    

class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
