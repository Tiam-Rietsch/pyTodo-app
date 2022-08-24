from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import datetime_safe, timezone
import math



class Category(models.Model):
    STATUS_CHOICES = (
        ('2', 'On progress'),
        ('3', 'Completed'),
        ('1', 'Empty'),
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='category_list')
    user_title = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default=STATUS_CHOICES[2][0])
    progress = models.IntegerField(default=0)
    created_on = models.DateField(default=timezone.now)
    slug = models.SlugField()        

    def __str__(self):
        return self.user_title

    def get_absolute_url(self):
        return reverse('cath_list')
    
    def is_new(self):
        return datetime_safe.date.today() == self.created_on
    
    def set_status(self):
        if len(self.task_list.all()) == 0:
            self.status = '1' # empty
        elif self.progress == 100:
            self.status = '3' # completed
        else:
            self.status = '2' # on progress
            
        self.save()

    # return the status wrt to the user's progress    
    def get_status(self):
        self.set_progress()
        self.set_status()
        return self.get_status_display()
        
    # calculate the user progress on the task category and save to database
    def set_progress(self):
        completed_tasks = self.task_list.filter(completed=True)
        total_tasks = self.task_list.all()
        if len(total_tasks) == 0:
            self.status =  '1'
            self. progress = 0
        else:
            done_percentage = (len(completed_tasks) / len(total_tasks)) * 100
            self.progress = math.ceil(done_percentage)
        self.save()
        
    def get_progress_deg(self):
        self.set_progress()
        self.set_status()
        return (self.progress/100)*360
        
    
    # return the user progress as a string
    def get_progress(self):
        self.set_status()        
        self.set_progress()
        if not self.status == '1':
            return str(self.progress)
        else:
            return "0"
