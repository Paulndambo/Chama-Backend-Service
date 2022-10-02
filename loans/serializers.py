from rest_framework import serializers
from .models import LoanApplication, Loan, LoanGuarantor, LoanPayment

class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = "__all__"


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"


class LoanGuarantorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanGuarantor
        fields = "__all__"


class LoanPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanPayment
        fields = "__all__"