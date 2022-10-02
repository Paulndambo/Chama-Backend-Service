from rest_framework import serializers
from .models import SavingContribution, Saving, MeriGoRoundContribution

class SavingContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingContribution
        fields = "__all__"


class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = "__all__"

class MeriGoRoundContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeriGoRoundContribution
        fields = "__all__"