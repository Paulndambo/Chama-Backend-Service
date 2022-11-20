from django.db import models
from api.core.models import LoanType
from api.users.models import Member
# Create your models here.

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

LOAN_REPAYMENT_CHOICES = (
    ("still_paying", "Still Paying"),
    ("full_paid", "Full Paid"),
    ("defaulted", "Defaulted"),
)

class LoanApplication(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_type = models.ForeignKey(LoanType, on_delete=models.CASCADE)
    amount_applying = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, default="pending", choices=LOAN_CHOICES)

    def __str__(self):
        return self.member.id_number


class Loan(models.Model):
    loan_application = models.OneToOneField(LoanApplication, on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_type = models.ForeignKey(LoanType, on_delete=models.CASCADE)
    amount_awarded = models.DecimalField(max_digits=20, decimal_places=2)
    amount_to_repay = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    total_interest = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    amount_repaid = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    status = models.CharField(max_length=100, choices=LOAN_REPAYMENT_CHOICES, default="still_paying")
    expected_last_pay_date = models.DateField(null=True, blank=True)
    date_applied = models.DateField()
    date_awarded = models.DateField()

    def __str__(self):
        return self.member.id_number


class LoanGuarantor(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    relationship = models.CharField(max_length=255)
    birth_date = models.DateField()
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=255, choices=MARITAL_STATUS)
    postal_code = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class LoanPayment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    payment_method = models.CharField(max_length=255, default="mpesa")
    date_paid = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.load.member.id_number