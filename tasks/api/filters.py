import django_filters
from tasks.models import Tarefa

class TarefaFilter(django_filters.FilterSet):
    status_tarefa = django_filters.ChoiceFilter(choices=Tarefa.StatusTarefa.choices)
    prioridade_tarefa = django_filters.ChoiceFilter(choices=Tarefa.PrioridadeTarefa.choices)
    class Meta:
        model = Tarefa
        fields = {
            'status_tarefa',
            'prioridade_tarefa',
            'id_secretaria',
            'tarefa_cargo',
            'id_criador',
        }
    