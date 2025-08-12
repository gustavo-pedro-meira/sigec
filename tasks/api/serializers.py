from rest_framework import serializers
from tasks.models import Tarefa
from registry.api.serializers import SecretariaSerializers, CargoSerializers
from accounts.api.serializers import FuncionarioSerializers

class TarefaSerializer(serializers.ModelSerializer):
    tarefa_cargo = CargoSerializers(read_only=True)
    id_secretaria = SecretariaSerializers(read_only=True)
    id_criador = FuncionarioSerializers(read_only=True)
    id_responsavel = FuncionarioSerializers(read_only=True)
    class Meta:
        model = Tarefa
        fields = ['id', 'missao_tarefa', 'descricao_tarefa', 'prazo_tarefa', 'status_tarefa', 'anexo_tarefa', 'prioridade_tarefa', 'id_secretaria', 'tarefa_cargo', 'id_criador', 'id_responsavel']
