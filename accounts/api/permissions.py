from rest_framework import permissions
from accounts.models import Funcionario
from django.utils import timezone

class CreateFuncionarioPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.cargo == 'S':
            print("Permissão concedida para o Secretário!")
        else:
            print("Acesso negado!")
            
class DataFuncionarioExpiraPermissions(permissions.BasePermission):
    message =  f'Sua conta expirou, passou do prazo de pagamentos. Entre em contato com o suporte.'
    
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        funcionario = Funcionario.objects.filter(id=request.user.id).first()
        if funcionario and funcionario.data_expiracao and funcionario.data_expiracao < timezone.now().date():
            return False
        return True