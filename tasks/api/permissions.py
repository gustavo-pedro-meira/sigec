from rest_framework import permissions

class CriarTarefaPermissions(permissions.BasePermission):
    message = 'Apenas usuários com cargo de Gestor ou Secretário podem criar tarefas.'
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user or not request.user.is_authenticated:
            return False
        
        return request.user.funcionario.cargo in ['G', 'S']