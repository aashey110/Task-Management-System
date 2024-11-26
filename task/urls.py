from rest_framework.routers import DefaultRouter
from django.urls import path, include
from viewset.task import TaskViewSet

# Create the router and register the ViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

# Include the router URLs
urlpatterns = [
    path('', include(router.urls)),
]