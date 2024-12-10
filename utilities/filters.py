from django_filters import rest_framework as filters
from task_app.models import Task

class TaskFilter(filters.FilterSet):
    due_date = filters.DateTimeFilter(field_name="due_date", lookup_expr="lte")

    class Meta:
        model = Task
        fields = ['status', 'due_date']
    