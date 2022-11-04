from django.db import models

# Create your models here.

# Cell : Cells of comment contents
class Cell(models.Model):
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')