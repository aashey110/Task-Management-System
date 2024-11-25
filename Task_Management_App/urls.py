from django.urls import path
from . import views
from .views import TaskDetail, TaskList

urlpatterns = [
    path('', views.index),
    path('signup/', views.signup, name='signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_home/', views.user_home, name='user_home'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('user_logout', views.user_logout, name='user_logout'),
    # path('task_api/<int:pk>/', views.task_api, name='task_api'),  #function based view
    # path('task_api/', views.task_api, name='task_api'),
    path('task/', TaskList.as_view()),      #class based view
    path('task/<int:pk>/', TaskDetail.as_view()),
    path('add_task/', views.add_task, name='add_task'),
    path('show_task/', views.show_task, name='show_task'),
]