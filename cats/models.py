# Create your models here.
from django.db import models


class Cat(models.Model):
    # ok, I think we need at least some length limit for a name
    # 200 should be pretty generous
    name = models.CharField(max_length=200)
    experience = models.PositiveIntegerField()
    # we will validate the breed using the api anyway
    # but I checked and the longest breed name seems to be 20-character-long
    breed = models.CharField(max_length=50)
    salary = models.PositiveIntegerField()

    def __str__(self):
        return self.name
