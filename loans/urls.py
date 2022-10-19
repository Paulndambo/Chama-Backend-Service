from django.urls import path, include
from .import views
#from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("loans", views.LoanModelViewSet, basename="loans")
router.register("loan-applications",
                views.LoanApplicationModelViewSet, basename="loan-applications")

loans_router = routers.NestedDefaultRouter(router, "loans", lookup="loan")
loans_router.register(
    "guarantors", views.LoanGuarantorsModelViewSet, basename="loan-guarantors")
loans_router.register("payments", views.LoanPaymentModelViewSet, basename="loan-payments")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(loans_router.urls))
    #path("", views.LoanAPIView.as_view(), name="loans"),
    #path("<int:pk>/", views.LoanRetrieveUpdateDestroyAPIView.as_view(), name="loan-details"),
    #path("loan-applications/", views.LoanApplicationAPIView.as_view(), name="loan-applications"),
    #path("loan-applications/<int:pk>/", views.LoanApplicationRetrieveUpdateDestroyAPIView.as_view(), name="loan-applications-details"),
    #path("guarantors/", views.LoanGuarantorAPIView.as_view(), name="guarantors"),
    #path("guarantors/<int:pk>/", views.LoanGuarantorRetrieveUpdateDestroyAPIView.as_view(), name="guarantor-details"),
    #path("loan-payments/", views.LoanPaymentAPIView.as_view(), name="loan-payments"),
]