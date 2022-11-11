from django.db import models

PRIORITY_STATUS = (
    ('low', 'LOW'),
    ('medium', 'MEDIUM'),
    ('height', 'HEIGHT')
)

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    files = models.FileField(upload_to='uploads/')
    URL = models.URLField(blank = True)
    priority = models.CharField(choices = PRIORITY_STATUS ,max_length = 30, default = 'low')

class Vote(models.Model):
    # Asocjacja
    tasks = models.ForeignKey(Tasks, on_delete = models.CASCADE)
    usersVote = models.TextField