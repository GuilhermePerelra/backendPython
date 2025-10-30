from django.urls import path
from carrinho import views

urlpatterns = [
    path('', views.visualizarCarrinho, name = 'carrinho'),
    path('adicionarItemCarrinho/<int:produto_id>/', views.adicionarItemCarrinho, name='adicionarItemCarrinho'),
    path('diminuirQuantidadeProduto/<int:produto_id>/', views.diminuirQuantidadeProduto, name='diminuirQuantidadeProduto'),
     path('removerItemCarrinho/<int:produto_id>/', views.removerItemCarrinho, name='removerItemCarrinho')

]