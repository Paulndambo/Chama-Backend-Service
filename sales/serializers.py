from rest_framework import serializers

class NewMemberOnboardingSerializer(serializers.Serializer):
    user_obj = serializers.JSONField()
    member_obj = serializers.JSONField()
    payment_obj = serializers.JSONField()
    employment_obj = serializers.JSONField()
    family_obj = serializers.JSONField()
    education_obj = serializers.JSONField()
    subscription_obj = serializers.JSONField()
    