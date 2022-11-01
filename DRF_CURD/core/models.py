from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    contact = models.CharField(max_length=12)
    city = models.CharField(max_length=150)

    def __str__(self):
        return self.name
