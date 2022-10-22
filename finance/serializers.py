from rest_framework import serializers
from .models import SavingContribution, Saving, MeriGoRoundContribution
from datetime import datetime

date_today = datetime.now()


class SavingContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingContribution
        fields = ["saving", "amount", "created"]


class CreateSavingContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingContribution
        fields = "__all__"


class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = "__all__"


class SavingsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        exclude = ["member", "year"]

    def create(self, validated_data):
        member_id = self.context['member_id']
        year = str(date_today.year)
        return Saving.objects.create(member_id=member_id, year=year, **validated_data)

class MeriGoRoundContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeriGoRoundContribution
        fields = "__all__"