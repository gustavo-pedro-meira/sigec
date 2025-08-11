from rest_framework import viewsets, serializers
from .serializers import TarefaSerializer
from tasks.models import Tarefa
from .permissions import CriarTarefaPermissions
from accounts.models import Funcionario

class TarefaViewSets(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [CriarTarefaPermissions]
    
    # def perform_create(self, serializer):
    #     try:
    #         funcionario_logado = self.request.user.funcionario
    #         serializer.save(id_criador=funcionario_logado)
    #     except Funcionario.DoesNotExist:
    #         raise serializers.ValidationError(
    #             {"detail": "Seu usuário não possui um perfil de funcionário associado. A operação não pode ser completada."}
    #         )