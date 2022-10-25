from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Saving, SavingContribution, MeriGoRoundContribution
from .serializers import SavingSerializer, SavingContributionSerializer, CreateSavingContributionSerializer, SavingsCreateSerializer, MeriGoRoundContributionSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class SavingAPIView(generics.GenericAPIView):
    queryset = Saving.objects.all()
    serializer_class = SavingSerializer

    def get(self, request, *args, **kwargs):
        savings = Saving.objects.all()
        serializer = self.serializer_class(instance=savings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SavingsModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Saving.objects.all()
    #serializer_class = SavingSerializer

    def get_serializer_context(self):
        return {"member_id": self.kwargs["member_pk"]}

    def get_serializer_class(self):
        if self.request.method == "POST":
            return SavingsCreateSerializer
        return SavingSerializer


class SavingContributionModelViewSet(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    #serializer_class = SavingContributionSerializer
    http_method_names = ["get", "post"]

    def get_serializer_context(self):
        return {"member_id": self.kwargs['member_pk']}

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateSavingContributionSerializer
        return SavingContributionSerializer

    def get_queryset(self):
        queryset = SavingContribution.objects.filter(member_id=self.kwargs['member_pk'])
        return queryset


class MemberMerigoRoundContributionModelViewSet(ModelViewSet):
    queryset = MeriGoRoundContribution.objects.all()
    serializer_class = MeriGoRoundContributionSerializer
    http_method_names = ["get", "post"]

    def get_serializer_context(self):
        return {"member_id": self.kwargs["member_pk"]}


    def get_queryset(self):
        return MeriGoRoundContribution.objects.filter(member_id=self.kwargs['member_pk'])

class MeriGoRoundContributionAPIView(generics.GenericAPIView):
    queryset = MeriGoRoundContribution.objects.all()
    serializer_class = MeriGoRoundContributionSerializer

    def get(self, request, *args, **kwargs):
        meri_go_round_contributions = MeriGoRoundContribution.objects.all()
        serializer = self.serializer_class(instance=meri_go_round_contributions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeriGoRoundContributionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MeriGoRoundContribution.objects.all()
    serializer_class = MeriGoRoundContributionSerializer

    lookup_field = "pk"


class SavingContributionAPIView(generics.GenericAPIView):
    queryset = SavingContribution.objects.all()
    serializer_class = SavingContributionSerializer

    def get(self, request, *args, **kwargs):
        saving_contributions = SavingContribution.objects.all()
        serializer = self.serializer_class(instance=saving_contributions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
