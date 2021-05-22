from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.
class Blog(models.Model):
    user=models.IntegerField()
    user_name=models.CharField(max_length=20)
    photo_main = models.ImageField(upload_to='photo/%Y/%m/%d/',blank=False)
    description = models.TextField(blank=False)
    privacy=models.BooleanField(default=False)

    def __str__(self):
        return self.user_name