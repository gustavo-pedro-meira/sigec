from django.db import models

# Create your models here.
class Secretaria(models.Model):
    nome_secretaria = models.CharField(max_length=200)
    setor_secretaria = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome_secretaria
    

class Cargo(models.Model):
    nome_cargo = models.CharField(max_length=150)
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome_cargo
    