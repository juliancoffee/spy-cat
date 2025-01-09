# Create your models here.
from django.db import models, IntegrityError


class Cat(models.Model):
    # ok, I think we need at least some length limit for a name
    # 200 should be pretty generous
    #
    # NOTE: name is not required to be unique here
    name = models.CharField(max_length=200)
    experience = models.PositiveIntegerField()
    # we will validate the breed using the api anyway
    # but I checked and the longest breed name seems to be 20-character-long
    breed = models.CharField(max_length=50)
    salary = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Mission(models.Model):
    # cat may be optional, but I don't think we can delete a cat while
    # they're still assigned to the mission
    #
    # that would be wrong ...
    cat = models.ForeignKey(Cat, on_delete=models.PROTECT, null=True)
    complete = models.BooleanField()

    def delete(self, *args, **kwargs):
        if self.cat is not None:
            raise IntegrityError("can't delete a mission with assigned cat")
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # TODO: check that cat doesn't have more than 3 missions
        super().save(*args, **kwargs)


class Target(models.Model):
    # NOTE: the same as with cats, name is not require to be unique here.
    # we differentiate them by id
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    notes = models.TextField()
    complete = models.BooleanField()

    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # TODO: check for note update while completed
        super().save(*args, **kwargs)
