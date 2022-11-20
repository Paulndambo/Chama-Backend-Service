from django.urls import path, include
from .import views 
from rest_framework_nested import routers
router = routers.DefaultRouter()
router.register("members", views.MemberModelViewSet, basename="members")

##Nested Routers
member_routers = routers.NestedDefaultRouter(router, "members", lookup="member")


urlpatterns = [
    path("", views.MemberProfileAPIView.as_view(), name="profile"),
    path("", include(router.urls)),
    path("", include(member_routers.urls)),
]