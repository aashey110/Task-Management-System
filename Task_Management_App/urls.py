from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signup/', views.signup, name='signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_home/', views.user_home, name='user_home'),
    path('user_logout', views.user_logout, name='user_logout')
]
