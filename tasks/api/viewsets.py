from rest_framework import viewsets, serializers
from .serializers import TarefaSerializer
from tasks.models import Tarefa
from .permissions import CriarTarefaPermissions
from .filters import TarefaFilter
from accounts.models import Funcionario

class TarefaViewSets(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [CriarTarefaPermissions]
    filterset_class = TarefaFilter