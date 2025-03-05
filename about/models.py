from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
