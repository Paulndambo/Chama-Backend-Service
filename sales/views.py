from django.shortcuts import render
from .serializers import NewMemberOnboardingSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from .mixins import NewMemberOnboardingMixin
# Create your views here.
class MemberOnboardingAPIView(generics.GenericAPIView):
    serializer_class = NewMemberOnboardingSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            #print(dict(serializer.validated_data))
            new_member_mixin = NewMemberOnboardingMixin(
                dict(serializer.validated_data))
            new_member_mixin.run()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)