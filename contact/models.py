from django.db import models

# Create your models here.


class Contact(models.Model):
    person = models.CharField(max_length=50)
    number = models.IntegerField()
