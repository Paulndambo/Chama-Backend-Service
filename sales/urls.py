from django.urls import path
from .import views

urlpatterns = [
    path("", views.MemberOnboardingAPIView.as_view(), name="member_onboarding"),
]