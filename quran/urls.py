from django.urls import path
from .views import (
    SuraListView,
    SuraDetailView,
    AyahDetailView,
    AyahListView,
    AuthorListView,
    QuranBookListView,
)

app_name = 'quran'

urlpatterns = [
    # Suralar
    path('suras/', SuraListView.as_view(), name='sura-list'),
    path('suras/<int:number>/', SuraDetailView.as_view(), name='sura-detail'),

    # Oyatlar
    path('ayahs/', AyahListView.as_view(), name='ayah-list'),
    path('suras/<int:sura_number>/ayahs/<int:ayah_number>/', AyahDetailView.as_view(), name='ayah-detail'),

    # Mualliflar
    path('authors/', AuthorListView.as_view(), name='author-list'),

    # Kitoblar
    path('books/', QuranBookListView.as_view(), name='book-list'),
]
