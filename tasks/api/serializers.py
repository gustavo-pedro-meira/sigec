from rest_framework import serializers
from tasks.models import Tarefa, Agenda
from registry.models import Secretaria, Cargo
from accounts.models import Funcionario
from registry.api.serializers import SecretariaSerializers, CargoSerializers
from accounts.api.serializers import FuncionarioSerializers
from django.utils import timezone
import datetime

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
            'status_tarefa', 'anexo_tarefa', 'prioridade_tarefa', 'hora_tarefa', 'pontuacao_tarefa',
            
            # Nomes dos campos de leitura 
            'id_secretaria',  'id_criador', 'id_responsavel',
            
            # Nomes dos campos de escrita 
            'secretaria_id', 'criador_id', 'responsavel_id', 'created_at', 'updated_at'
        ]
        
    # Validações Personalizadas
    def PrazoTarefaDataMaiorQueHojeValidation(self, data):
        if data['prazo_tarefa'] < datetime.date.today():
            raise serializers.ValidationError('O prazo da tarefa não pode ser uma data passada.')
        return data
    
    def validate(self, data):
        self.PrazoTarefaDataMaiorQueHojeValidation(data)
        # self.HorarioAgendaMaiorQueAgoraValidation(data)
        return data
    
    
    
class AgendaSerializers(serializers.ModelSerializer):
    # Campo de Leitura
    id_criador = FuncionarioSerializers(read_only=True)
    
    # Campos de Escrita
    criador_id = serializers.PrimaryKeyRelatedField(queryset=Funcionario.objects.all(), source='id_criador', write_only=True)
    
    class Meta:
        model = Agenda
        fields = [
            'id', 'motivo_agenda', 'local_agenda',
            'data_agenda', 'hora_agenda', 'status_agenda',
            
            # Campo Leitura
            'id_criador',
            
            # Campo Escrita
            'criador_id'
        ]
        
    # Validações Personalizadas
    def DataAgendaMaiorQueHojeValidation(self, data):
        if data['data_agenda'] < datetime.date.today():
            raise serializers.ValidationError('O prazo da tarefa não pode ser uma data passada.')
        return data
    
    def validate(self, data):
        self.DataAgendaMaiorQueHojeValidation(data)
        # self.HorarioAgendaMaiorQueAgoraValidation(data)
        return data