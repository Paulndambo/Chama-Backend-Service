from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import LoanTypeSerializer, MembershipSerializer
from .models import Membership, LoanType
# Create your views here.
class MembershipAPIView(generics.GenericAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

    def get(self, request, *args, **kwargs):
        memberships = Membership.objects.all()
        serializer = self.serializer_class(instance=memberships, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data 
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanTypeAPIView(generics.GenericAPIView):
    queryset = LoanType.objects.all()
    serializer_class = LoanTypeSerializer

    def get(self, request, *args, **kwargs):
        loan_types = LoanType.objects.all()
        serializer = self.serializer_class(instance=loan_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)