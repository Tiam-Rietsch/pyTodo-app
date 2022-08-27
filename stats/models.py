from django.db import models
from django.utils import timezone
from users.models import CustomUser
from tasks.models import Task


#  MANAGER
class DailyProgressManager(models.Manager):
    def create_instance(self, logged_user):
        # first checks if the if there there is no model instance of the the same date
        objects = DailyProgress.objects.filter(user=logged_user, date=timezone.now().date())
        if len(objects) == 0:
            UD = logged_user.username + " - " + str(timezone.now().date())
            new_progress = self.create(
                user_date=UD,
                date=timezone.now().date(),
                user=logged_user,
            )
            return new_progress
        else:
            return None


# MODEL
class DailyProgress(models.Model):
    user_date = models.CharField(primary_key=True, max_length=100) # username + date of the instance (UD)
    date = models.DateField(default=timezone.now().date())
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    n_completed = models.IntegerField(default=0) # number of tasks completed
    n_expired = models.IntegerField(default=0) # number of tasks expired
    n_querying = models.IntegerField(default=0) # number of tasks In progress

    objects = DailyProgressManager() # set the object manager
    
    def __str__(self):
        return self.user.username + " - " + str(self.date)


    # creates a new model instance
    @classmethod
    def add_instance(cls, logged_user):
        new = cls.objects.create_instance(logged_user)
        if not new == None:
            new.save()
            
     
    # reset the databese values for all instances that match the user   
    @classmethod
    def refresh_database(cls, logged_user):
        progress = cls.objects.get(user=logged_user, date=timezone.now().date())
        progress.reset_instance(logged_user)          

    
    # reset the value of n_completed, n_expired, n_querying
    def reset_instance(self, logged_user):
        expired = 0
        completed = 0
        querying = 0
        for task in Task.objects.filter(author=logged_user):
            if task.is_completed:
                completed += 1
            elif task.is_expired:
                expired += 1
            elif task.is_querying:
                querying += 1
                
        self.n_expired = expired
        self.n_completed = completed
        self.n_querying = querying
        self.save()
