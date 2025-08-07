from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Funcionario(User):  
    CARGO = (
        ('F', 'Funcionário'),
        ('S', 'Secretário'),
        ('G', 'Gestor')
    )
    
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(default='2000-02-02')
    numero = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11)
    genero = models.CharField(max_length=20)
    estado_civil = models.CharField(max_length=20)
    secretaria_trabalho = None
    cargo = models.CharField(max_length=20, choices=CARGO, default='F')