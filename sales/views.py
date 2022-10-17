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
            data = {
                "membership": row[1],
                "user_obj": {
                    "email": row[2],
                    "username": row[3],
                    "first_name": row[4],
                    "last_name": row[5]
                },
                "member_obj": {
                    "id_number": row[7],
                    "phone_number": row[6],
                    "kra_pin": row[8],
                    "birth_date": datetime.strptime(row[9], '%m-%d-%Y').date(),
                    "gender": row[10],
                    "marital_status": row[11],
                    "postal_code": row[12],
                    "town": row[13],
                    "country": row[14],
                    "status": row[15]
                },
                "payment_obj": {
                    "payment_method": row[16],
                    "mpesa_number": row[17],
                    "preferred_payment_day": row[18]
                },
                "employment_obj": {
                    "employment_status": row[19],
                    "employment_sector": row[20],
                    "salary": row[21],
                    "total_deductions": row[22],
                    "employer": row[23],
                    "position": row[24],
                    "date_employed": datetime.strptime(row[25], '%m-%d-%Y').date(),
                    "previous_employer": row[26],
                    "previous_salary": row[27]
                },
                "family_obj": {
                    "name": row[28],
                    "phone_number": row[29],
                    "email": row[30],
                    "relationship": row[31],
                    "birth_date": datetime.strptime(row[32], '%m-%d-%Y').date(),
                    "gender": row[33],
                    "marital_status": row[34],
                    "postal_code": row[35],
                    "town": row[36],
                    "country": row[37]
                },
                "education_obj": {
                    "highest_education_level": row[38],
                    "last_school_attended": row[39],
                    "year_joined": row[40],
                    "graduation_year": row[41],
                    "course": row[42],
                    "grade": row[43]
                },
                "subscription_obj": {
                    "subscription_title": row[44],
                    "rate": row[45]
                }
            }
            new_member_mixin = NewMemberOnboardingMixin(data)
            new_member_mixin.run()
            print(data)
        
        return Response("Hello World!")