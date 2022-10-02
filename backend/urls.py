from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('sales.urls')),
    path("api/users/", include("users.urls")),
    path('api/auth/', include('rest_authtoken.urls')),
    path("api/finance/", include('finance.urls')),
    path("api/loans/", include('loans.urls')),
]
