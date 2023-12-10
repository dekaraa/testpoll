from django.db import models

# Create your models here.
class PollModel(models.Model):
    question = models.TextField()
    p1 = models.CharField(max_length=30)
    p2 = models.CharField(max_length=30)
    p3 = models.CharField(max_length=30)
    p1c = models.IntegerField(default=0)
    p2c = models.IntegerField(default=0)
    p3c = models.IntegerField(default=0)
    
    def __str__(self):
        return self.question
        
    