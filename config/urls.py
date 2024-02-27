"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(
      title="Quran Online API",
      default_version='v2',
      description="Bu api orqali siz quronu karimning oyatlari suralari va ma'nolarini topishingiz mumkin. Audiolari bilan birga",
      terms_of_service="https://t.me/asadbek_074/",
      contact=openapi.Contact(email="asadbekoffical1202@gmail.com"),

   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)





urlpatterns = [
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('jet/', include('jet.urls', 'jet')),
    path('api/v2/admin/', admin.site.urls),
    path('api/auth/login/uz/', include('rest_framework.urls')),
    path('api/v2/uz/', include('quran_uz.urls')), #Lang uz
    path('api/v2/arabic/', include('quran_arabic.urls')), #Lang arabic
    path('api/v2/english/', include('quran_eng.urls')), #Lang english
    path('api/v2/rus/', include('quran_ru.urls')), # Lang rus
    path('api/v2/book/', include('quran_books.urls')),
    path('api/v2/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v2/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v2/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


