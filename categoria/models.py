from django.db import models

class Categoria(models.Model):
    categoria_nome = models.CharField(max_length=80, unique=True)
