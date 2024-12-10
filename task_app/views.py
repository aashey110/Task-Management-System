from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet
from rest_framework import  filters
from django_filters.rest_framework import DjangoFilterBackend



from .models import Task
from .serializers import TaskSerializer
from utilities.filters import TaskFilter





class TaskModelView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = TaskFilter
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]



















#APIView


# class TaskList(APIView):
#     permission_classes = [IsAdminUser]
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = TaskFilter
      
#     def get(self, request):
#         filterset = TaskFilter(request.GET, queryset=Task.objects.all())
#         if not filterset.is_valid():
#             return Response(filterset.errors, status=400)
        
#         tasks = filterset.qs
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
        
# class TaskDetail(APIView):
#     permission_classes = [IsAuthenticated, IsAdminUser]

#     def get(self, request, pk):
#         task = Task.objects.get(pk=pk)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         task = Task.objects.get(pk=pk)
#         if task.assign_to != request.user:
#             raise PermissionDenied("You are not authorized to update this task.")
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#     def delete(self, request, pk):
#         task = Task.objects.get(pk=pk)
#         if not request.user.is_staff():
#             raise PermissionDenied("You are not authorized to delete this task.")
#         task.delete()
#         return Response({"message": "Task deleted"})













































#View Set

# Create your views here.
# class TaskViewSet(ViewSet):

#     def list(self, request):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#     def update(self, request, pk):
#         task = Task.objects.get(pk=pk)
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
    
#     def retrieve(self, request, pk):
#         task = Task.objects.get(pk=pk)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
    
#     def destroy(self, request, pk):
#         task = Task.objects.get(pk=pk)
#         task.delete()
#         return Response({"message": "Task deleted"})






































