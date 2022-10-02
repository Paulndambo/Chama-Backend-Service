from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.db import transaction
from users.models import Member, Employment, Subscription, MpesaDetail, Education, FamilyMember

date_today = datetime.now().date()
renew_date = date_today + timedelta(days=366)

class NewMemberOnboardingMixin(object):
    
    def __init__(self, data):
        self.data = data

    def run(self):
        self.__onboard_new_member()
        

    ## TODO: create an atomic transaction here

    @transaction.atomic
    def __onboard_new_member(self):
        try:
            self.__create_user()
            self.__create_member()
            self.__create_eduction_detail()
            self.__create_family_member()
            self.__create_mpesa_detail()
            self.__create_employemt_detail()
            self.__create_member_subscription()
        except Exception as e:
            raise e

    """Create User Object"""
    def __create_user(self):
        user_obj = self.data['user_obj']
        password = "1234"
        user = User.objects.create(**user_obj)
        user.set_password(password)
        user.save()
        print("New User Created!!!!")

    def __create_member(self):
        email = self.data['user_obj']['email']
        member_obj = self.data['member_obj']
        user = User.objects.filter(email=email).first()
        print("User Object...:", user)
        member = Member.objects.create(**member_obj, renew_date=renew_date, user=user)
        member.save()
        print("New Member created successfully!!!")

    def __create_family_member(self):
        member_id = self.data['member_obj']['id_number']
        member = Member.objects.filter(id_number=member_id).first()
        family_obj = self.data['family_obj']
        family_member = FamilyMember.objects.create(**family_obj, member=member)
        family_member.save()
        print("Family Member Created Successfully")


    def __create_mpesa_detail(self):
        member_id = self.data['member_obj']['id_number']
        member = Member.objects.filter(id_number=member_id).first()
        payment_obj = self.data['payment_obj']
        payment = MpesaDetail.objects.create(**payment_obj, member=member)
        payment.save()
        print("Member Mpesa Detail Added Successfully!!!")
    
    def __create_eduction_detail(self):
        member_id = self.data['member_obj']['id_number']
        member = Member.objects.filter(id_number=member_id).first()
        education_obj = self.data['education_obj']
        education = Education.objects.create(**education_obj, member=member)
        education.save()
        print("Member Education Created Successfully!!!!")

    def __create_employemt_detail(self):
        member_id = self.data['member_obj']['id_number']
        member = Member.objects.filter(id_number=member_id).first()
        employment_obj = self.data['employment_obj']
        employment = Employment.objects.create(**employment_obj, member=member)
        employment.save()
        print("Member Employment Details Created")

    def __create_member_subscription(self):
        member_id = self.data['member_obj']['id_number']
        member = Member.objects.filter(id_number=member_id).first()
        member_subscription_obj = self.data['subscription_obj']
        member_subscription = Subscription.objects.create(**member_subscription_obj, member=member)
        member_subscription.save()
        print("Member subscription created successfully!!!")
