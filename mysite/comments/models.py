from django.db import models
from django.contrib import admin
import datetime 
from django.utils import timezone
from django.contrib import admin

# Create your models here.

#Theme
class Theme(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.title

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?'
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



# Cell : Cells of comment contents
class Cell(models.Model):
    theme = models.ForeignKey(Theme, related_name='cells', on_delete=models.CASCADE)
    
    publisher_name = models.CharField(max_length=20)
    comment_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published')

    