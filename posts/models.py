from django.db import models

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
        


class Post(TimeStamp):
    title = models.CharField(max_length=300)
    body = models.TextField()
    
    def __str__(self):
        return self.title
