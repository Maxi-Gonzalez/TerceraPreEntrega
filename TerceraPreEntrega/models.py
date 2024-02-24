from django.db import models

# Create your models here.
class Cafe(models.Model):
    nombre=models.CharField(max_length=40)
    precio= models.IntegerField()

