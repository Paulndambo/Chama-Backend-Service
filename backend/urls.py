from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title="Chama Cloud SaaS API",
        default_version='v1',
        description="This is the Chama Backend Service",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="paulkadabo@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("sales/", include('sales.urls')),
    path("users/", include("apps.users.urls")),
    path("finance/", include('apps.finance.urls')),
    path("loans/", include('apps.loans.urls')),
    path("core/", include('apps.core.urls')),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.jwt')),
    path("", schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    path("redoc/", schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),
]
