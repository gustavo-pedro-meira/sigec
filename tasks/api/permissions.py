from rest_framework import permissions

class CriarTarefaPermissions(permissions.BasePermission):
    message = 'Apenas usuários com cargo de Gestor ou Secretário podem criar tarefas.'
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user or not request.user.is_authenticated:
            return False
        
        return request.user.funcionario.cargo in ['G', 'S']
    
    # def has_object_permission(self, request, view, obj):
    #     if request.user.funcionario.cargo == 'G':
    #         return True
        
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
        
    #     self.message = 'Você só pode alterar ou deletar tarefas que você mesmo criou.'
    #     return obj.id_criador == request.user.funcionario
