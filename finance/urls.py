from django.urls import path, include
from .import views
from users.urls import member_routers
member_routers.register("savings", views.SavingsModelViewSet, basename="member-savings")
member_routers.register("saving-contributions",
                        views.SavingContributionModelViewSet, basename="saving-contributions")

urlpatterns = [
    path("", include(member_routers.urls)),
    #path("savings/", views.SavingAPIView.as_view(), name="savings"),
    #path("meri-go-round-contributions/", views.MeriGoRoundContributionAPIView.as_view(), name="meri-go-round-contributions"),
    #path("meri-go-round-contributions/<int:pk>/", views.MeriGoRoundContributionRetrieveUpdateDestroyAPIView.as_view(), name="meri-go-round-contributions-details"),
    #path("savings-contributions/", views.SavingContributionAPIView.as_view(), name="savings-contributions"),
]