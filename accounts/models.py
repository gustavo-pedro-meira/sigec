from django.db import models
from django.contrib.auth.models import User
from registry.models import Secretaria, Cargo
from django.utils import timezone
# Create your models here.
class Funcionario(User):  
    class CargoFuncionario(models.TextChoices):
        # FUNCIONARIO = 'F', 'Funcionário'
        SECRETARIO = 'S', 'Secretario'
        PREFEITO = 'P', 'Prefeito'
        DIRETOR = 'D', 'Diretor'
        TECNICO = 'T', 'Tecnico'
        COORDENADOR = 'C', 'Coordenador'
        
    class GeneroFuncionario(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'
        NAO_DIZER = 'PF', 'Prefiro não dizer'
    
    nome_completo = models.CharField(max_length=100)
    data_nascimento = models.DateField(default='2000-02-02', blank=True, null=True)
    genero = models.CharField(max_length=20, choices=GeneroFuncionario.choices, default=GeneroFuncionario.NAO_DIZER)
    cargo = models.CharField(max_length=20, choices=CargoFuncionario.choices, default=CargoFuncionario.SECRETARIO)
    secretaria_trabalho = models.ForeignKey(Secretaria, on_delete=models.SET_NULL, related_name='secretarias', null=True, blank=True)
    data_expiracao = models.DateField(default=timezone.now)
    pontuacao_tarefas = models.IntegerField(default=0, blank=True, null=True)
    # cargo_trabalho = models.ForeignKey(Cargo, on_delete=models.SET_NULL, related_name='cargos', null=True, blank=True)
    # tarefas = models.ForeignKey('tasks.Tarefa', on_delete=models.SET_NULL, related_name='tarefas', blank=True, null=True)
    
    def __str__(self):
        return self.nome_completo
    