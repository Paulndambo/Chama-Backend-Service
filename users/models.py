from django.db import models
from django.contrib.auth.models import User
from core.models import Membership

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

class Member(models.Model):
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255, unique=True)
    kra_pin = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=255, choices=MARITAL_STATUS)
    postal_code = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    renew_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id_number

    
    @property
    def employment(self):
        employment = self.employment_set.all().values(
            "id",
            "employment_status",
            "employment_sector",
            "salary",
            "total_deductions",
            "employer",
            "date_employed",
            "position",
            "previous_employer",
            "previous_salary"
        )
        return employment

    @property
    def education(self):
        education = self.education_set.all().values(
            "id",
            "highest_education_level",
            "last_school_attended",
            "year_joined",
            "graduation_year",
            "course",
            "grade"
        )
        return education

    @property
    def subscription(self):
        subscription = self.subscription_set.all().values(
            "id",
            "subscription_title",
            "rate",
            "start_date",
            "renew_date",
            "cancellation_allowed",
            "cancellation_reason",
            "status"
        )
        return subscription


    @property
    def mpesa_detail(self):
        
        mpesa_detail = MpesaDetail.objects.filter(member__id=self.id).values(
            "id",
            "payment_method",
            "mpesa_number",
            "preferred_payment_day"
        )
        return mpesa_detail #{"message": "No mpesa detail available"}
    
    @property
    def family_member(self):
        family_member = self.familymember_set.all().values(
            "id",
            "name",
            "relationship",
            "gender",
            "birth_date",
            "email",
            "phone_number",
            "postal_code",
            "town",
            "country"
        )
        if family_member:
            return family_member
        return {"message": "No family member"}


class Employment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    employment_status = models.CharField(max_length=255)
    employment_sector = models.CharField(max_length=255, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    employer = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    date_employed = models.DateField(null=True, blank=True)
    previous_employer = models.CharField(max_length=255, null=True, blank=True)
    previous_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.member.id_number

SUBSCRIPTION_CHOICES = (
    ("weekly", "Weekly"),
    ("monthly", "Monthly"),
)

class Subscription(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    subscription_title = models.CharField(max_length=255, choices=SUBSCRIPTION_CHOICES)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cancellation_allowed = models.BooleanField(default=True)
    cancellation_reason = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    renew_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.member.id_number


class Education(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    highest_education_level = models.CharField(max_length=255)
    last_school_attended = models.CharField(max_length=255)
    year_joined = models.CharField(max_length=255, null=True, blank=True)
    graduation_year = models.CharField(max_length=255, null=True, blank=True)
    course = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.member.id_number


class MpesaDetail(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=200)
    mpesa_number = models.CharField(max_length=200)
    preferred_payment_day = models.CharField(max_length=200)

    def __str__(self):
        return self.member.id_number

class FamilyMember(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=255, unique=True)
    email = models.EmailField(null=True, blank=True)
    relationship = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=255, choices=MARITAL_STATUS)
    postal_code = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    renew_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
