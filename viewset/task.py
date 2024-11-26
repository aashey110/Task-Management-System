from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from task.models import Task
from serializers.task import TaskSerializer
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
from custom_user.models import CustomUser
from django.contrib import messages
from utilities.filters import TaskFilter
from rest_framework.viewsets import ModelViewSet





class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter] 
    # filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer




