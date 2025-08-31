from django.db import models
from django.utils import timezone
from registry.models import Secretaria, Cargo
from accounts.models import Funcionario
from django.utils import timezone

# Create your models here.
class BaseModelQuerySet(models.QuerySet):
    def delete(self):
        self.update(deleted_at=timezone.now() , is_active=False)

class BaseManager(models.Manager):
    def get_queryset (self):
        return BaseModelQuerySet( self.model, using=self._db).filter( deleted_at__isnull =True, is_active=True)

class BaseModel(models.Model):
    created_at = models.DateTimeField( auto_now_add =True)
    updated_at = models.DateTimeField( auto_now=True)
    deleted_at = models.DateTimeField( editable=False, blank=True, null=True)
    is_active = models.BooleanField( editable=False, default=True)
    
    objects = BaseManager()
    
    class Meta:
        abstract = True
    
    def delete(self, **kwargs):
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()
        
    def hard_delete (self, **kwargs):
        super(BaseModel, self).delete(**kwargs)

class Tarefa(BaseModel):
    class StatusTarefa(models.TextChoices):
        A_FAZER = 'AF', 'A Fazer'
        EM_ANDAMENTO = 'A', 'Andamento'
        CONLUIDA = 'C', 'Concluída'
        EXPIRADA = 'E', 'Expirada'
        
    class PrioridadeTarefa(models.TextChoices):
        BAIXA = 'B', 'Baixa'
        MEDIA = 'M', 'Médio'
        ALTA = 'A', 'Alta'
        URGENTE = 'U', 'Urgente'
    
    missao_tarefa = models.CharField(max_length=150)
    descricao_tarefa = models.TextField(blank=True, null=True)
    prazo_tarefa = models.DateField(default=timezone.now)
    hora_tarefa = models.TimeField(default=timezone.now, blank=True, null=True)
    status_tarefa = models.CharField(max_length=20, choices=StatusTarefa.choices, default=StatusTarefa.A_FAZER)
    anexo_tarefa = models.FileField(upload_to='documentos/', blank=True, null=True)
    prioridade_tarefa = models.CharField(max_length=20, choices=PrioridadeTarefa.choices, default=PrioridadeTarefa.BAIXA)
    id_secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE, related_name='tarefas')
    tarefa_cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, related_name='taredas_cargo', blank=True, null=True)
    id_criador = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, related_name='tarefas_criado', blank=True, null=True)
    id_responsavel = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='tarefas_responsavel', blank=True, null=True)
    
    def __str__(self):
        return self.missao_tarefa
    
class Agenda(BaseModel):
    class StatusAgenda(models.TextChoices):
        AGENDADO = 'A', 'Agendado'
        ADIADO = 'AD', 'Adiado'
        REAGENDADO = 'RA', 'Reagendado'
        ENCERRADO = 'E', 'Encerrado'
        CANCELADO = 'C', 'Cancelado'
        REALIZADO = 'R', 'Realizado'
        
    motivo_agenda = models.CharField(max_length=200)
    descricao_agenda = models.TextField(blank=True, null=True)
    local_agenda = models.CharField(max_length=150, blank=True, null=True)
    data_agenda = models.DateField(default=timezone.now)
    hora_agenda = models.TimeField(default=timezone.now, blank=True, null=True)
    status_agenda = models.CharField(max_length=20, choices=StatusAgenda.choices, default=StatusAgenda.AGENDADO, blank=True, null=True)
    id_criador = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='agendas_criador')
    
    def __str__(self):
        return self.motivo_agenda