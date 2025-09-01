from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Funcionario

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