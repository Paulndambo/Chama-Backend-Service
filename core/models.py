from django.db import models

# Create your models here.
class Membership(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class LoanType(models.Model):
    name = models.CharField(max_length=255)
    maximum_amount = models.DecimalField(max_digits=10, decimal_places=2)
    minimum = models.DecimalField(max_digits=10, decimal_places=2)
    repayment_days = models.IntegerField()
    number_of_guarators = models.IntegerField()
    minimum_savings = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name