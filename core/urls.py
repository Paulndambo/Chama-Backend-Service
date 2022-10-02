from django.urls import path
from .import views

urlpatterns = [
    path("loan-types/", views.LoanTypeAPIView.as_view(), name="loan-types"),
    path("memberships/", views.MembershipAPIView.as_view(), name="memberships"),
]