from rest_framework import viewsets
from .serializers import SecretariaSerializers, CargoSerializers
from registry.models import Secretaria, Cargo
from rest_framework.permissions import IsAuthenticated

class SecretariaViewSets(viewsets.ModelViewSet):
    queryset = Secretaria.objects.all()
    serializer_class = SecretariaSerializers
    permission_classes = [IsAuthenticated]
    
class CargoViewSets(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializers
    permission_classes = [IsAuthenticated]