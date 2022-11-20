from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import MemberProfileSerializer, MemberSerializer
from django.contrib.auth.models import User
from .models import Member
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class MemberProfileAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = MemberProfileSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        #member_id = kwargs['member_id']
        if user.is_staff:
            members = Member.objects.all()
            serializer = self.serializer_class(instance=members, many=True)
        else:
            members = Member.objects.filter(user=user).first()
            serializer = self.serializer_class(instance=members)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MemberModelViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer