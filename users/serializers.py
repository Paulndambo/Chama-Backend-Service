from rest_framework import serializers
from .models import Member, Education, FamilyMember, MpesaDetail, Employment, Subscription
from django.contrib.auth.models import User

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = "__all__"


class MpesaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaDetail
        fields = "__all__"


class EmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employment
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class MemberProfileSerializer(serializers.ModelSerializer):
    #education = EducationSerializer()
    #subscription = SubscriptionSerializer()
    #mpesa_detail = MpesaDetailSerializer()
    #family_member = FamilyMemberSerializer(read_only=True)
    #employment = serializers.SerializerMethodField(read_only=True)
    user_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Member
        fields = [
            "id", 
            "id_number",
            "phone_number",
            "kra_pin",
            "birth_date",
            "gender",
            "marital_status",
            "postal_code",
            "town",
            "country",
            "status",
            "renew_date",
            "created",
            "updated",
            "education", 
            "subscription",
            "family_member",
            "employment",
            "user_data",
            "mpesa_detail"
        ]

    def get_user_data(self, obj):
        return {
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name,
            "username": obj.user.username,
            "email": obj.user.email
        }

    
    
    