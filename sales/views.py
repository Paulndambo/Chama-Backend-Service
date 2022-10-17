from django.shortcuts import render
from .serializers import NewMemberOnboardingSerializer, BulkMembersOnboardingSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from .mixins import NewMemberOnboardingMixin
from datetime import datetime

import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='temp')
from .utils import bulk_member_onboarding
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


class BulkMembersOnboardingAPIView(generics.CreateAPIView):
    serializer_class = BulkMembersOnboardingSerializer


    def post(self, request, *args, **kwargs):
        serialiazer = self.serializer_class(data=request.data)
        serialiazer.is_valid(raise_exception=True)
        file = serialiazer.validated_data['members_file']
        content = file.read()
        file_content = ContentFile(content)
        file_name = fs.save(
            "temp.csv", file_content
        )
        temp_file = fs.path(file_name)
        csv_file = open(temp_file, errors='ignore')
        reader = csv.reader(csv_file)
        next(reader)
        teachers_list = []

        for row in reader:
            data = bulk_member_onboarding(row)
            new_member_mixin = NewMemberOnboardingMixin(data)
            new_member_mixin.run()
            print(data)
        
        return Response({"success": "Members Uploaded Successfully!!"}, status=status.HTTP_201_CREATED)