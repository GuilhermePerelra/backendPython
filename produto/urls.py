from django.urls import path
from produto import views

urlpatterns = [
    path('', views.visualizarProduto, name='produto'),
    path('<slug:categoria_slug>/<slug:produto_slug>/',
         views.detalharProduto, name = 'detalhar_produto')
]
