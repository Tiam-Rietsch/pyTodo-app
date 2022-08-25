from django.contrib import admin
from .models import DailyProgress

class DailyProgressInline(admin.TabularInline):
    model = DailyProgress
    extra = 0

admin.site.register(DailyProgress)
