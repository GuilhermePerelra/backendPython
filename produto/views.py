from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def visualizarProduto(request):
    return HttpResponse('visualizando produto')