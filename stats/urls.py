from django.urls import path 
from .views import dash_board_view

urlpatterns = [ 
    path('dashboard/', dash_board_view, name="stats_detail")
]