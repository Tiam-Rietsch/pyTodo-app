from django.shortcuts import render
from .models import DailyProgress

def dash_board_view(request):
    if request.method == 'GET':
        template_name = 'stats/stats_detail.html'
        DailyProgress.add_instance(request.user)
        DailyProgress.refresh_database(request.user)
            
        return render(request, template_name=template_name)
