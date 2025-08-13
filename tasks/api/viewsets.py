from rest_framework import viewsets, serializers
from .serializers import TarefaSerializer
from tasks.models import Tarefa
from .permissions import CriarTarefaPermissions
from .filters import TarefaFilter
from accounts.models import Funcionario
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class TarefaViewSets(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [CriarTarefaPermissions]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = TarefaFilter
    ordering_fields = ['prazo_tarefa']
       
    def get_queryset(self):
        user = self.request.user

        if user.funcionario.cargo in ['G', 'S']:
            return Tarefa.objects.all()
        
        if user.funcionario.cargo == 'F':

            if not user.funcionario.cargo_trabalho:
                return Tarefa.objects.none()
            return Tarefa.objects.filter(cargo_destino=user.funcionario.cargo_trabalho)

        return Tarefa.objects.none()

    # def perform_create(self, serializer):
    #     serializer.save(criador=self.request.user)