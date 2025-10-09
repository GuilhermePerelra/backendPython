from django.http import HttpResponse
from django.shortcuts import redirect, render

from produto.forms import ProdutoForm
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

def adicionarProduto(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        return redirect('/')
    dicionario = {
        'formulario' : form,
    }
    
    return render(request, 'produto/adicionar.html', dicionario)