from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('quran/uz/', quran_uz, name='book-uz'),
    path('quran/ru/', quran_ru, name='book-ru'),
    path('quran/eng/', quran_eng, name='book-eng'),
    path('quran/arabic/', quran_arabic, name='book-arabic')

]
