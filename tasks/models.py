from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone


class Task(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='task_list')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    dead_line = models.DateTimeField(blank=False, null=False, default=timezone.now)
    completed = models.BooleanField(default=False,)
    
    class Meta:
        ordering = ('dead_line',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cat_list')

    @property
    def is_querying(self):
        return timezone.now() < self.dead_line and not self.completed
    
    @property
    def is_completed(self):
        return self.completed

    @property
    def is_expired(self):
        return timezone.now() >= self.dead_line and not self.completed
    
    @property
    def get_status(self):
        if self.is_querying:
            return "Querying"
        elif self.is_completed:
            return "Completed"
        elif self.is_expired:
            return "Expired"