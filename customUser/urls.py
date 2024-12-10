from django.urls import path, include

from . import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('profile/<int:pk>/', views.ProfileAPIView.as_view(), name='profile'),
    path('api-auth', include('rest_framework.urls')),

]
