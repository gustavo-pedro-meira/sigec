from django.db import models
from django.contrib.auth.models import User
from registry.models import Secretaria, Cargo
# from tasks.models import Tarefa

# Create your models here.
class Funcionario(User):  
    class CargoFuncionario(models.TextChoices):
        FUNCIONARIO = 'F', 'Funcionário'
        SECRETARIO = 'S', 'Secretario'
        GESTOR = 'G', 'Gestor'
    
    nome_completo = models.CharField(max_length=100)
    # data_nascimento = models.DateField(default='2000-02-02')
    # genero = models.CharField(max_length=20)
    cargo = models.CharField(max_length=20, choices=CargoFuncionario.choices, default=CargoFuncionario.FUNCIONARIO)
    secretaria_trabalho = models.ForeignKey(Secretaria, on_delete=models.SET_NULL, related_name='secretarias', null=True, blank=True)
    cargo_trabalho = models.ForeignKey(Cargo, on_delete=models.SET_NULL, related_name='cargos', null=True, blank=True)
    # tarefas = models.ForeignKey('tasks.Tarefa', on_delete=models.SET_NULL, related_name='tarefas', blank=True, null=True)
    
    def __str__(self):
        return self.nome_completo
    