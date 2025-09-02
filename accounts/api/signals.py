from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from accounts.models import Funcionario
from tasks.models import Tarefa

# Sinal para atualizar a data de expiração de todos os funcionários quando o cargo Prefeito for alterado o campo dataa expiracao
@receiver(post_save, sender=Funcionario)
def atualizar_data_expiracao_funcionarios(sender, instance, created, update_fields, **kwargs):
    if created:
        return
    
    if instance.cargo == 'P':
        foi_alterada_data = update_fields is None or 'data_expiracao' in update_fields
        
        if foi_alterada_data:
            nova_data = instance.data_expiracao
            
            if nova_data:
                qs = Funcionario.objects.exclude(pk=instance.pk)
                qs.update(data_expiracao=nova_data)
                
@receiver(post_save, sender=Tarefa)
def atualizar_pontuacao_responsavel(sender, instance, created, update_fields, **kwards):
    if created:
        return
    if instance.status_tarefa == 'C':
        foi_alterada_status = update_fields is None or 'status_tarefa' in update_fields
        
        if foi_alterada_status:
            responsavel = instance.id_responsavel
            responsavel.pontuacao_tarefas = (responsavel.pontuacao_tarefas or 0) + instance.pontuacao_tarefa
            responsavel.save(update_fields=['pontuacao_tarefas'])
            
    elif instance.status_tarefa == 'E':
        foi_alterada_status = update_fields is None or 'status_tarefa' in update_fields
        
        if foi_alterada_status:
            responsavel = instance.id_responsavel
            responsavel.pontuacao_tarefas = (responsavel.pontuacao_tarefas or 0) - instance.pontuacao_tarefa
            if responsavel.pontuacao_tarefas < 0:
                responsavel.pontuacao_tarefas = 0
            responsavel.save(update_fields=['pontuacao_tarefas'])
            
@receiver(pre_delete, sender=Tarefa)
def remover_pontuacao_responsavel(sender, instance, **kwargs):
    if instance.id_responsavel:
        responsavel = instance.id_responsavel
        responsavel.pontuacao_tarefas = (responsavel.pontuacao_tarefas or 0) - instance.pontuacao_tarefa
        if responsavel.pontuacao_tarefas < 0:
            responsavel.pontuacao_tarefas = 0
        responsavel.save(update_fields=['pontuacao_tarefas'])