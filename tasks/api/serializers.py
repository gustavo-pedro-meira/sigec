from rest_framework import serializers
from tasks.models import Tarefa
from accounts.api.serializers import FuncionarioSerializers
from registry.api.serializers import SecretariaSerializers

class TarefaSerializer(serializers.ModelSerializer):
    tarefa_usuario = FuncionarioSerializers(read_only=True)
    id_secretaria = SecretariaSerializers(read_only=True)
    class Meta:
        model = Tarefa
        fields = ['id', 'missao_tarefa', 'descricao_tarefa', 'prazo_tarefa', 'status_tarefa', 'anexo_tarefa', 'prioridade_tarefa', 'id_secretaria', 'tarefa_usuario']
        # read_only = ['id_criador']