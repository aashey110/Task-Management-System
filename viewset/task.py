from rest_framework import generics
from task.models import Task
from serializers.task import TaskSerializer
from rest_framework import  filters
from django_filters.rest_framework import DjangoFilterBackend
from utilities.filters import TaskFilter
from rest_framework.viewsets import ModelViewSet
from utilities.permissions import IsAdminOrReadOnly 
from rest_framework.permissions import IsAuthenticated




class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter] 
    # filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer