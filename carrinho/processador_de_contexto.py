from carrinho.models import CarItem, Carrinho
from carrinho.views import _getCarId


def contador(request):
    contador = 0
    try:
        car = Carrinho.objects.filter(car_id = _getCarId(request))
        car_items = CarItem.objects.all().filter(car = car[:1])
        for car_item in car_items:
            contador += car_item.quantidade
    except Carrinho.DoesNotExist:
        contador = 0  
    return dict(contador = contador)