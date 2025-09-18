from django.urls import path
from produto import views

urlpatterns = [
    path('', views.visualizarProduto, name='produto'),
]
