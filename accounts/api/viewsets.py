from rest_framework import viewsets
from .serializers import FuncionarioSerializers
from accounts.models import Funcionario
from rest_framework.permissions import IsAuthenticated

class FuncionarioViewSets(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializers
    permission_classes = [IsAuthenticated]