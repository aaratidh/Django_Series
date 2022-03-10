from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model): #eachh class going to be each table in the database
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now) 
    author = models.ForeignKey(User, on_delete = models.CASCADE)


    # auto_now_add you cant update the value of the post
    # to manage the value used the default as pass timezone as the value 
    # this function wil take the time from the current time zone
    # we need to run the migration to update the database in Django 
    
    

