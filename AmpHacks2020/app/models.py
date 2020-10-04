"""
Definition of models.
"""

from django.db import models

# Create your models here.


class StoreData(models.Model):
    revenue = models.IntegerField
    date = models.DateField
    # rent = models.IntegerField
    # rent_freq = models.CharField(max_length=20)
    # util = models.IntegerField
    # util_freq = models.CharField(max_length=20)
    staff_hours = models.FloatField
    staff_salary = models.FloatField
    sell_cost = models.FloatField
    num_sold = models.IntegerField

    def __str__(self):
        return self.revenue
