from rest_framework.routers import DefaultRouter
from django.urls import path, include
from viewset.custom_user import UserViewSet

# Create a router
router = DefaultRouter()

# Register the ViewSet
router.register(r'user', UserViewSet, basename='user')

# Include the router URLs
urlpatterns = [
    path('', include(router.urls)),
    
]
