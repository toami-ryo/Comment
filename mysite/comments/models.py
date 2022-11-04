from django.db import models

# Create your models here.

#Theme
class Theme(models.Model):
    title = models.CharField(max_length=50)



# Cell : Cells of comment contents
class Cell(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')