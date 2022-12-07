from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class events(models.Model):

    status_choices = {
        ('C', 'Completed'),
        ('P', 'Pending'),
    }

    host=models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    event_name=models.CharField(max_length=100)
    datetime=models.DateTimeField()
    invited_user=models.ForeignKey(User,models.CASCADE)
    status=models.CharField(max_length=2,choices=status_choices)

class invites(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    event=models.ForeignKey(events,on_delete=models.CASCADE)

class invited(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    event=models.ForeignKey(events,on_delete=models.CASCADE,related_name='event')
