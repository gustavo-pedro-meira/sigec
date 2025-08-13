from rest_framework import serializers
from tasks.models import Tarefa
from registry.models import Secretaria, Cargo
from accounts.models import Funcionario
from registry.api.serializers import SecretariaSerializers, CargoSerializers
from accounts.api.serializers import FuncionarioSerializers

class TarefaSerializer(serializers.ModelSerializer):
    # Somente Leitura
    id_secretaria = SecretariaSerializers(read_only=True)
    id_criador = FuncionarioSerializers(read_only=True)
    id_responsavel = FuncionarioSerializers(read_only=True)
    
    # Somente Escrita
    secretaria_id = serializers.PrimaryKeyRelatedField(queryset=Secretaria.objects.all(), source='id_secretaria', write_only=True)
    criador_id = serializers.PrimaryKeyRelatedField(queryset=Funcionario.objects.all(), source='id_criador', write_only=True)
    responsavel_id = serializers.PrimaryKeyRelatedField(queryset=Funcionario.objects.all(), source='id_responsavel', write_only=True)

    class Meta:
        model = Tarefa
        fields = [
            'id', 'missao_tarefa', 'descricao_tarefa', 'prazo_tarefa', 
            'status_tarefa', 'anexo_tarefa', 'prioridade_tarefa', 
            
            # Nomes dos campos de leitura (objetos completos)
            'id_secretaria',  'id_criador', 'id_responsavel',
            
            # Nomes dos campos de escrita (apenas IDs)
            'secretaria_id', 'criador_id', 'responsavel_id'
        ]