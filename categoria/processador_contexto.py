from categoria.models import Categoria

def categoria_display(request):
    display = Categoria.objects.all()
    return dict(cats = display)