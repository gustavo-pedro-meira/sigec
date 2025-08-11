from rest_framework import serializers
from registry.models import Secretaria, Cargo

class SecretariaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Secretaria
        fields = ['id', 'nome_secretaria', 'setor_secretaria']
        
class CargoSerializers(serializers.ModelSerializer):
    secretaria = SecretariaSerializers(read_only=True)
    class Meta:
        model = Cargo
        fields = ['id', 'nome_cargo', 'secretaria']