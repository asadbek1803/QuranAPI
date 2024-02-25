from django.urls import path, include
from .views import read_quran, SuraList

urlpatterns = [
    path('api/quran/online-read/',  read_quran, name='quran-online-read'),
    path('api/quran/sura/<str:name>/<int:sura_number>/', SuraList.as_view(), name='quran-sura')
]