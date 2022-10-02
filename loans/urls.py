from django.urls import path
from .import views

urlpatterns = [
    path("", views.LoanAPIView.as_view(), name="loans"),
    path("<int:pk>/", views.LoanRetrieveUpdateDestroyAPIView.as_view(), name="loan-details"),
    path("loan-applications/", views.LoanApplicationAPIView.as_view(), name="loan-applications"),
    path("loan-applications/<int:pk>/", views.LoanApplicationRetrieveUpdateDestroyAPIView.as_view(), name="loan-applications-details"),
    path("guarantors/", views.LoanGuarantorAPIView.as_view(), name="guarantors"),
    path("guarantors/<int:pk>/", views.LoanGuarantorRetrieveUpdateDestroyAPIView.as_view(), name="guarantor-details"),
    path("loan-payments/", views.LoanPaymentAPIView.as_view(), name="loan-payments"),
]