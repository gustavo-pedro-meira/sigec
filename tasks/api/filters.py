import django_filters
from tasks.models import Tarefa, Agenda

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
            'id_responsavel',
        }
    
class AgendaFilter(django_filters.FilterSet):
    status_agenda = django_filters.ChoiceFilter(choices=Agenda.StatusAgenda.choices)
    class Meta:
        model = Agenda
        fields = {
            'status_agenda',
            'id_criador',
            'data_agenda'
        }