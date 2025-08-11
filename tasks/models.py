from django.db import models
from django.utils import timezone
from registry.models import Secretaria
from accounts.models import Funcionario

# Create your models here.
class Tarefa(models.Model):
    class StatusTarefa(models.TextChoices):
        A_FAZER = 'AF', 'A Fazer'
        EM_ANDAMENTO = 'A', 'Andamento'
        CONLUIDA = 'C', 'Concluída'
        EXPIRADA = 'E', 'Expirada'
        
    class PrioridadeTarefa(models.TextChoices):
        URGENTE = 'U', 'Urgente'
        ALTA = 'A', 'Alta'
        MEDIA = 'M', 'Médio'
        BAIXA = 'B', 'Baixa'
    
    missao_tarefa = models.CharField(max_length=150)
    descricao_tarefa = models.TextField()
    prazo_tarefa = models.DateTimeField(default=timezone.now)
    status_tarefa = models.CharField(max_length=20, choices=StatusTarefa.choices, default=StatusTarefa.A_FAZER)
    anexo_tarefa = models.FileField(upload_to='documentos/', blank=True, null=True)
    prioridade_tarefa = models.CharField(max_length=20, choices=PrioridadeTarefa.choices, default=PrioridadeTarefa.BAIXA)
    id_secretaria = models.OneToOneField(Secretaria, on_delete=models.CASCADE, related_name='tarefas')
    tarefa_usuario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, related_name='taredas_usuario', blank=True, null=True)
    
    def __str__(self):
        return self.missao_tarefa