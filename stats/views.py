from audioop import reverse
from django.shortcuts import render
from .models import DailyProgress
from plotly.offline import plot
from categories.models import Category
from tasks.models import Task
import plotly.express as px
import pandas as pd


def dash_board_view(request):
    if request.method == 'GET':
        template_name = 'stats/stats_detail.html'
        DailyProgress.add_instance(request.user)
        DailyProgress.refresh_database(request.user)
        
         #---------------------Bar chart
        qs = Category.objects.filter(author=request.user)
        bar_data = {
            "titles": [cat.title for cat in qs],
            "Querying": [
                len([ task for task in cat.task_list.all() if task.is_querying]) for cat in qs
            ],
            "Expired": [
                len([ task for task in cat.task_list.all() if task.is_expired]) for cat in qs
            ],
            "Completed": [
                len([ task for task in cat.task_list.all() if task.is_completed]) for cat in qs
            ]
        }
        
        #----------------------LineChart
        qs = DailyProgress.objects.filter(user=request.user).order_by('date')
        line_data = {
            "titles": [str(progress.date) for progress in qs],
            "querying_progress": [progress.n_querying for progress in qs],
            "expired_progress": [progress.n_expired for progress in qs],
            "completed_progress": [progress.n_completed for progress in qs]
        }
        
        #---------------------PieChart
        qs = Task.objects.filter(author=request.user)
        pie_data = {
            "titles": ["Querying", "Expired", "Completed"],
            "data": [
                len([task for task in qs if task.is_querying]),
                len([task for task in qs if task.is_expired]),
                len([task for task in qs if task.is_completed]),
            ]
        }
        
        context = {
            "bar_data": bar_data,
            "line_data": line_data,
            "pie_data": pie_data
        }
        return render(request, template_name, context)
