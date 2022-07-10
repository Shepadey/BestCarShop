from django.db import models
from pkg_resources import safe_name
class Example(models.Model):
    name = models.CharField(max_length=120)
    color = models.CharField(max_length=120)
    cost = models.IntegerField()

    def __str__(self) :
        return self.name
        
    

# Create your models here.
