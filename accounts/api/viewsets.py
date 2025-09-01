from rest_framework import viewsets
from .serializers import FuncionarioSerializers
from accounts.models import Funcionario
from rest_framework.permissions import IsAuthenticated
from accounts.api.filters import FuncionarioFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class FuncionarioViewSets(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializers
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = FuncionarioFilter
    ordering_fields = ['pontuacao_tarefas']
    