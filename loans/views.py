from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import LoanApplication, Loan, LoanGuarantor, LoanPayment
from .serializers import LoanGuarantorSerializer, LoanPaymentSerializer, LoanSerializer, LoanApplicationSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.
class LoanApplicationAPIView(generics.GenericAPIView):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer

    def get(self, request, *args, **kwargs):
        loan_applications = LoanApplication.objects.all()
        serializer = self.serializer_class(instance=loan_applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanApplicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer

    lookup_field = "pk"

class LoanModelViewSet(ModelViewSet):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()


class LoanGuarantorsModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LoanGuarantorSerializer

    def get_serializer_context(self):
        return {"loan_id": self.kwargs["loan_pk"]}
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return LoanGuarantor.objects.filter(loan_id=self.kwargs["loan_pk"])
        return LoanGuarantor.objects.filter(loan_id=self.kwargs["loan_pk"]).filter(member__user=user)
    


class LoanAPIView(generics.GenericAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def get(self, request, *args, **kwargs):
        loans = Loan.objects.all()
        serializer = self.serializer_class(instance=loans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    lookup_field = "pk"


class LoanGuarantorAPIView(generics.GenericAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


    def get(self, request, *args, **kwargs):
        guarantors = LoanGuarantor.objects.all()
        serializer = self.serializer_class(instance=guarantors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanGuarantorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    lookup_field = "pk"


class LoanPaymentAPIView(generics.GenericAPIView):
    queryset =LoanPayment.objects.all()
    serializer_class = LoanPaymentSerializer

    def get(self, request, *args, **kwargs):
        payments = LoanPayment.objects.all()
        serializer = self.serializer_class(instance=payments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

class LoanPaymentModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LoanPaymentSerializer

    def get_serializer_context(self):
        return {"loan_id": self.kwargs["loan_pk"]}

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return LoanPayment.objects.filter(loan_id=self.kwargs['loan_pk'])
        return LoanPayment.objects.filter(loan_id=self.kwargs['loan_pk']).filter(member__user=user)
