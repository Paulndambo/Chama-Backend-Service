from django.urls import path
from .import views 

urlpatterns = [
    path("", views.MemberProfileAPIView.as_view(), name="profile"),
]