from tkinter.ttk import Style
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
