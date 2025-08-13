from rest_framework import serializers
from registry.models import Secretaria, Cargo

class SecretariaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Secretaria
        fields = ['id', 'nome_secretaria', 'setor_secretaria']
        
class CargoSerializers(serializers.ModelSerializer):
    # Campo Leitura
    secretaria = SecretariaSerializers(read_only=True)
    
    # Campo Escrita
    secretaria_id = serializers.PrimaryKeyRelatedField(queryset=Secretaria.objects.all(), source='secretaria', write_only=True)
    class Meta:
        model = Cargo
        fields = [
            'id', 'nome_cargo', 
            
            # Campo Leitura
            'secretaria',
            
            # Campo Escrita
            'secretaria_id'
        ]