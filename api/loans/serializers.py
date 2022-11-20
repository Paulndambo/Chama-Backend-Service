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
        fields = ["id", "name", "member", "id_number", "email", "relationship", 
                "birth_date", "gender", "marital_status", "postal_code", "town", "country" ]

    def create(self, validated_data):
        loan_id = self.context['loan_id']
        return LoanGuarantor.objects.create(loan_id=loan_id, **validated_data)


class LoanPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanPayment
        fields = ["id", "amount", "member", "payment_method", "date_paid"]

    def create(self, validated_data):
        loan_id = self.context['loan_id']
        return LoanPayment.objects.create(loan_id=loan_id, **validated_data)