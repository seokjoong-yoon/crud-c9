from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    writer = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now())
    body = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'images/', blank = True)