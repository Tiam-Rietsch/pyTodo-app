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
        
        # ------------------------------------------PIE CHART
        qs = Task.objects.filter(author=request.user).order_by("created_on")
        pie_data_frame = [
            {
                "title": "Querying",
                "value": (len([task for task in qs if task.is_querying])/len(qs)) * 100,
            },
            {
                "title": "Expired",
                "value": (len([task for task in qs if task.is_expired])/len(qs)) * 100,
            },
            {
                "title": "Completed",
                "value": (len([task for task in qs if task.is_completed])/len(qs)) * 100,
            },
        ]
        
        pie_df = pd.DataFrame(pie_data_frame)
        pie_figure = px.pie(pie_df, values="value", names="title", color="title", color_discrete_map={"Completed": "#00CC96", "Querying": "#636EFA", "Expired": "#EF553B"})
        pie_chart = plot(pie_figure, output_type="div")
        
        # ------------------------------------------BAR CHART
        qs = Category.objects.filter(author=request.user).order_by("-title")
        bar_data_frame = [
            {
                "Category": cat.title,
                "Querying": len([task for task in Task.objects.filter(category=cat) if task.is_querying]),
                "Expired": len([task for task in Task.objects.filter(category=cat) if task.is_expired]),
                "Completed": len([task for task in Task.objects.filter(category=cat) if task.is_completed]),
            } for cat in qs 
        ]
        
        bar_df = pd.DataFrame(bar_data_frame)
        bar_figure = px.bar(bar_df, x="Category", y=["Completed", "Querying", "Expired"], color_discrete_map={"Completed": "#00CC96", "Querying": "#636EFA", "Expired": "#EF553B"})
        bar_figure.update_layout(title="Categories status", xaxis_title="Categories", yaxis_title="Number of tasks")
        
        bar_chart = plot(bar_figure, output_type="div")
        
        # ------------------------------------------LINE CHART
        # create a data frame
        qs = DailyProgress.objects.filter(user=request.user).order_by("date")
        line_data_frame = [ 
            {
                "date": date_values.date,
                "querying": date_values.n_querying,
                "expired": date_values.n_expired,
                "completed": date_values.n_completed,   
            } for date_values in qs
        ]
        line_df = pd.DataFrame(line_data_frame)
        
        # create the line chart figure
        line_figure = px.line(line_df, x="date", y=["querying", "expired", "completed"], markers=True)
        line_figure.update_layout(title="Daily Progress", yaxis_title="Number of tasks")
        
        # plot the figure as a div
        line_chart = plot(line_figure, output_type="div")
        
        context = {
            "line_chart_2": line_chart,
            "line_chart": line_chart,
            "bar_chart": bar_chart,
            "pie_chart": pie_chart
        }
        return render(request, template_name, context)
