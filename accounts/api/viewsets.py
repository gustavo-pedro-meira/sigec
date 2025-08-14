from rest_framework import viewsets
from .serializers import FuncionarioSerializers
from accounts.models import Funcionario
from rest_framework.permissions import IsAuthenticated
from accounts.api.filters import FuncionarioFilter
from django_filters.rest_framework import DjangoFilterBackend


class FuncionarioViewSets(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializers
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = FuncionarioFilter