from django.urls import path, include
from rest_framework.routers import DefaultRouter


from . import views


router = DefaultRouter()

router.register('task', views.TaskModelView, basename='task')


urlpatterns = [
    path('', include(router.urls)),
    # path('task/', views.TaskList.as_view()),
    # path('task/<int:pk>', views.TaskDetail.as_view()),
    path('api-auth', include('rest_framework.urls')),
]
