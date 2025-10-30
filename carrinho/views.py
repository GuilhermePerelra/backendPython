from django.shortcuts import get_object_or_404, redirect, render

from carrinho.models import CarItem, Carrinho
from produto.models import Produto
from django.core.exceptions import ObjectDoesNotExist


# obtendo a sessao e vinculando a car.

def _getCarId(request):
    car = request.session.session_key
    
    if not car:
        car = request.session.create()
    return car    

def visualizarCarrinho(request, total=0, quantidade=0, items=None):
    try:
        carrinho = Carrinho.objects.get(car_id = _getCarId(request))
        items = CarItem.objects.filter(car = carrinho, esta_disponivel=True)
        for item in items:
            total += (item.produto.preco * item.quantidade)
            quantidade += item.quantidade
    except ObjectDoesNotExist:    
        print("objeto nao existe")
        pass
    
    contexto_item = {
        'total' : total,
        'quantidade' : quantidade,
        'items' : items,
    }
    return render(request, 'loja/carrinho.html', contexto_item)

def adicionarItemCarrinho(request, produto_id):
    #localizando o produto com o parametro "produto_id"
    produto = Produto.objects.get(id = produto_id)
    
    #criar o carrinho para adicionar o produto
    try:
        carrinho = Carrinho.objects.get(car_id = _getCarId(request))
    except Carrinho.DoesNotExist:
        carrinho = Carrinho.objects.create(
            car_id = _getCarId(request)
        )    
    carrinho.save()
    
    try:
        car_item = CarItem.objects.get(produto = produto, car = carrinho)
        car_item.quantidade += 1
        car_item.save()
    except CarItem.DoesNotExist:
        car_item = CarItem.objects.create(
            produto = produto,
            car = carrinho, 
            quantidade = 1,
        )    
        car_item.save()
    return redirect('carrinho')

def diminuirQuantidadeProduto(request, produto_id):
    carrinho = Carrinho.objects.get(car_id = _getCarId(request))
    produto = get_object_or_404(Produto, id=produto_id)
    car_item = CarItem.objects.get(produto=produto, car = carrinho)
    print(car_item.quantidade)
    if car_item.quantidade > 1:
        car_item.quantidade -= 1
        car_item.save()
    else:
        car_item.delete()
    return redirect('carrinho')

def removerItemCarrinho(request, produto_id):
    car = Carrinho.objects.get(car_id =  _getCarId(request))
    produto = get_object_or_404(Produto, id=produto_id)
    car_item = CarItem.objects.get(produto = produto, car=car)
    car_item.delete()
    return redirect('carrinho')