from django.db import models

class Categoria(models.Model):
     nome = models.CharField(max_length=100)

     def __str__(self):
          return self.nome

class Produto(models.Model):
     Categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
     nome =  models.CharField(max_length=100)
     preço = models.DecimalField(max_digits=10, decimal_places=6)
     imagem = models.ImageField(upload_to='media')
     def __str__(self):
          return self.nome