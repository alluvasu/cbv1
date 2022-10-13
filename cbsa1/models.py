from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    pages=models.IntegerField()
    

# Create your models here.
