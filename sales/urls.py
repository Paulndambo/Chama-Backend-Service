from django.urls import path
from .import views

urlpatterns = [
    path("", views.MemberOnboardingAPIView.as_view(), name="member_onboarding"),
    path("bulk-onboarding", views.BulkMembersOnboardingAPIView.as_view(),
         name="bulk-onboarding"),
]