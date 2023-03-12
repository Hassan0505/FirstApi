from django.db import models


# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    year = models.IntegerField()
    types = models.TextChoices('types', 'SUV Sport Sedan')

    def __str__(self):
        return self.name
