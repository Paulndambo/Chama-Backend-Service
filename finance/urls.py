from django.urls import path
from .import views

urlpatterns = [
    path("savings/", views.SavingAPIView.as_view(), name="savings"),
    path("meri-go-round-contributions/", views.MeriGoRoundContributionAPIView.as_view(), name="meri-go-round-contributions"),
    path("meri-go-round-contributions/<int:pk>/", views.MeriGoRoundContributionRetrieveUpdateDestroyAPIView.as_view(), name="meri-go-round-contributions-details"),
    path("savings-contributions/", views.SavingContributionAPIView.as_view(), name="savings-contributions"),
]