"""
URL konfiguratsiyasi — Quran API v3
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    # ── Bosh sahifa ───────────────────────────────
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    # ── Admin panel ──────────────────────────────
    path('admin/', admin.site.urls),

    # ── API v3 (unified) ──────────────────────────
    path('api/v3/', include('quran.urls')),

    # ── Swagger / OpenAPI dokumentatsiyasi ────────
    path('api/v3/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v3/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v3/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
