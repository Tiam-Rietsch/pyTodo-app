from django import forms
from  django.contrib.admin.widgets import AdminSplitDateTime
from .models import Task


class TaskCreateForm(forms.ModelForm):
    '''This form is used for the TaskCreateView'''

    # setting the required widget for the datetime
    dead_line = forms.SplitDateTimeField(widget=AdminSplitDateTime)
    
    class Meta:
        model = Task
        fields = ('title', 'dead_line', 'description',)
    


class TaskUpdateForm(forms.ModelForm):
    '''This form is used for the TaskUpdateView'''

    class Meta:
        model = Task 
        fields = ('completed', 'title', 'description')


class TaskResetForm(forms.ModelForm):
    '''This form is used for the taskResetView'''

    # setting the required widget for the datetime
    dead_line = forms.SplitDateTimeField(widget=AdminSplitDateTime)

    class Meta:
        model = Task
        fields = ('dead_line',)


class AdminTaskForm(forms.ModelForm):
    '''This form is used in the admin setion for tasks'''

    # setting the required widget for the datetime
    dead_line = forms.SplitDateTimeField(widget=AdminSplitDateTime)

    class Meta:
        model = Task
        fields = ('__all__')
