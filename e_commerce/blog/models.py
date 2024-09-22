from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=70)
    descrption = models.TextField()
    image = models.ImageField( upload_to='blog/')