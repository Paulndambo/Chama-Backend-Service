from django.db import models
from api.users.models import Member
from django.contrib.auth.models import User


CONTRIBUTION_STATUS = (
    ("pending", "Pending"),
    ("paid", "Paid"),
    ("defaulted", "Defaulted"),
    ("future", "Future"),
)

GENDER_CHOICES = (
    ("male", "Male"),
    ("female", "Female"),
)

STATUS_CHOICES = (
    ("active", "Active"),
    ("disabled", "Disabled"),
    ("inactive", "Inactive"),
    ("banned", "Banned"),
)

MARITAL_STATUS = (
    ("single", "Single"),
    ("married", "Married"),
    ("divorced", "Divorced"),
    ("widowed", "Widowed"),
)

LOAN_CHOICES = (
    ("declined", "Declined"),
    ("approved", "Approved"),
    ("pending", "Pending"),
)

# Create your models here.
class Saving(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    amount_saved = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    interest_earned = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_savings = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.member.id_number


class SavingContribution(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    saving = models.ForeignKey(Saving, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.member.id_number


class MeriGoRoundContribution(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    status = models.CharField(max_length=255, choices=CONTRIBUTION_STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.member.id_number
