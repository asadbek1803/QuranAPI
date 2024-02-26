from django.urls import path
from .views import SuraList
app_name = 'quran_uz'
urlpatterns = [
    path('uz/quran/<int:pk>/', SuraList.as_view(), name='list')
]