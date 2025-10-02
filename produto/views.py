from django.http import HttpResponse
from django.shortcuts import render

from produto.models import Produto

# Create your views here.
def visualizarProduto(request,):
    return HttpResponse('visualizando produto')

def detalharProduto(request, categoria_slug, produto_slug):
    produto = Produto.objects.get(slug = produto_slug
                                    , categoria__slug = categoria_slug)
    
    contexto= {
        'prod' : produto
    }
    
    return render(request, 'loja/produto_detalhe.html', contexto)