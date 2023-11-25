from django.shortcuts import render
from .models import Produto,Categoria
from django.contrib.auth.decorators import login_required


@login_required
def mercado(request):
     produtos = Produto.objects.all()
     return render(request, 'mercado.html',{'produtos':produtos})
@login_required
def produto(request, id):
     produto = Produto.objects.get(id=id)
     return render(request, 'produto.html',{produto:produto})
def remove(request, id):
     remove = Produtos.objects.get(id=id)
     remove.delete()
     return render(request, 'mercado.html',{'remove':remove})
