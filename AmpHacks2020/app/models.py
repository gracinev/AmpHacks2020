"""
Definition of models.
"""

from django.db import models

# Create your models here.

from django.db import models


class PredResults(models.Model):

    Revenue = models.FloatField()
    Cost = models.FloatField()
    Lease = models.FloatField()
    Product = models.FloatField()
    Utilities = models.FloatField()
    Assets = models.FloatField()
    analyzedResult = models.CharField(max_length=50)

    def __str__(self):
        return self.analyzedResult