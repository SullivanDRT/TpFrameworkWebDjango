from django.db import models

# Create your models here.

class Book(models.Model):
    titre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    year = models.DateField()
    isbn = models.IntegerField()
    backCover = models.CharField(max_length=300)
    cover = models.BooleanField()



