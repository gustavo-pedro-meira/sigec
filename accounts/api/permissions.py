from rest_framework import permissions
from accounts.models import Funcionario

class CreateFuncionarioPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.cargo == 'S':
            print("Permissão concedida para o Secretário!")
        else:
            print("Acesso negado!")