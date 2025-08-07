from rest_framework import viewsets
from .serializers import FuncionarioSerializers
from accounts.models import Funcionario

class FuncionarioViewSets(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializers