import django_filters
from accounts.models import Funcionario

class FuncionarioFilter(django_filters.FilterSet):
    cargo = django_filters.ChoiceFilter(choices=Funcionario.CargoFuncionario.choices)
    
    class Meta:
        model = Funcionario
        fields = {
            'cargo',
            'nome_completo',
            'secretaria_trabalho',
        }