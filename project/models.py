from django.db import models
from datetime import datetime

# Create your models here.

class Project_log(models.Model):
    user    = models.CharField(max_length=35)
    date    = models.DateField(default=datetime.today)
    cost_center = models.CharField(max_length=10)
    prod_grp    = models.CharField(max_length=10)
    project     = models.CharField(max_length=10)
    hours   = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    notes   = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.pk} USER: {self.user}, PVM: {self.date}, KP : {self.cost_center}, PROJECT: {self.project},'
