from rest_framework import serializers
from accounts.models import Funcionario
from django.contrib.auth.models import User
import re

class FuncionarioSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, style = {'input_type': 'password'})
    class Meta:
        model = Funcionario
        fields = ['id', 'cargo', 'email', 'username', 'password']
        
    # Validações Personalizadas
    def SenhaCaracteresEspeciaisValidation(self, data):
        caracteres = ['!', '#', '$', '%', '@', '^', '*', '&']
        if not any(c in data['password'] for c in caracteres):
            raise serializers.ValidationError('A senha deve conter pelo menos 1 caractere especial.')
        return data
    
    def Senha8DigitosValidation(self, data):
        if len(data['password']) < 8:
            raise serializers.ValidationError('A senha deve conter pelo menos 8 caracteres.')
        return data
    
    def SenhaComNumeroValidation(self, data):
        if not re.search(r'[0-9]', data['password']):
            raise serializers.ValidationError('A senha deve conter pelo menos 1 número.')
        return data
    
    def SenhaLetraMaiusculaValidation(self, data):
        if not re.search(r'[A-Z]', data['password']):
            raise serializers.ValidationError('A senha deve conter pelo 1 letra maiúscula.')
        return data
        
        
    def SenhaSemEspacoValidation(self, data):
        if " " in data['password']:
            raise serializers.ValidationError("A senha não dever conter espaço.")
        return data
    
    def validate(self, data):
        self.SenhaCaracteresEspeciaisValidation(data)
        self.Senha8DigitosValidation(data)
        self.SenhaComNumeroValidation(data)
        self.SenhaLetraMaiusculaValidation(data)
        self.SenhaSemEspacoValidation(data)
        return data
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = Funcionario(**validated_data) 
        user.set_password(password)  
        user.clean()
        user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.clean()
        instance.save()
        return instance