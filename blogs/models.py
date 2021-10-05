from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=50,blank=False)
    desc= models.CharField(max_length=300,blank=False) 
    posts = models.Manager()  