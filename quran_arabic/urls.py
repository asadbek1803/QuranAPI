from django.urls import path
from .views import *

urlpatterns = [
    path('quran/<int:pk>/', SuraList.as_view(), name='sura-list-arabic'),
    path('quran/<int:pk>/<int:oyat_number>/', SuraDetail.as_view(), name='oyat-detail-arabic')
]