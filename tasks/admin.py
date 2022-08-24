from django.contrib import admin
from .forms import AdminTaskForm
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    form = AdminTaskForm


admin.site.register(Task, TaskAdmin)
