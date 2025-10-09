from django import forms

from produto.models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('categoria', 'produto_nome', 'descricao','preco', 'estoque', 'imagem', 'slug', 'esta_disponivel')