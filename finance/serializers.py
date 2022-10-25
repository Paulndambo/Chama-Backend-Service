from rest_framework import serializers, status, response
from .models import SavingContribution, Saving, MeriGoRoundContribution
from datetime import datetime
from django.db import transaction
date_today = datetime.now()
from decimal import Decimal


class SavingContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingContribution
        fields = ["saving", "amount", "created"]


class CreateSavingContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingContribution
        fields = ["amount", "created"]


    @transaction.atomic
    def create(self, validated_data):
        member_id = self.context.get("member_id")
        year = str(date_today.year)
        member_savings = Saving.objects.filter(member_id=member_id).filter(year=year).first()
        member_savings.amount_saved += Decimal(validated_data['amount'])
        member_savings.save()

        contribution = SavingContribution()
        contribution.member_id = member_id
        contribution.saving_id = member_savings.id 
        contribution.amount = validated_data['amount']
        contribution.save()
        return response.Response({"success": "Contribution Successfully Saved!!"}, status=status.HTTP_201_CREATED) #SavingContribution.objects.filter(member_id=member_id, saving_id=member_savings.id, **validated_data)


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
        fields = ["amount", "status", "created"]

    
    def create(self, validated_data):
        member_id = self.context['member_id']
        return MeriGoRoundContribution.objects.create(member_id=member_id, **validated_data)