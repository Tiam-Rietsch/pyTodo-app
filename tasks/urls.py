from django.urls import path 
from .views import TaskCreateView, TaskDeleteView, TaskUpdateView, TaskResetView

urlpatterns = [ 
    path('<int:pk>/reset/', TaskResetView.as_view(), name='task_reset'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('<slug:slug>/add/', TaskCreateView.as_view(), name='task_create'),
]