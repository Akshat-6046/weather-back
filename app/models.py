from django.db import models

# Create your models here.
class Countries(models.Model):
    name=models.CharField(max_length=50)
    iso3=models.CharField(max_length=3)
    unicodeFlag=models.TextField()
    
    