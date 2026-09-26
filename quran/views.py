from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Sura, Ayah, Author, QuranBook
from .serializers import (
    SuraListSerializer, SuraDetailSerializer,
    AyahSerializer, AuthorSerializer, QuranBookSerializer
)
from .filters import SuraFilter, AyahFilter

CACHE_TTL = 60 * 15  # 15 daqiqa cache


# ─────────────────────────────────────────────
# Suralar ro'yxati  GET /api/v3/suras/
# ─────────────────────────────────────────────
@extend_schema(tags=["Suralar"])
class SuraListView(generics.ListAPIView):
    """
    Barcha suralar ro'yxati.
    Filter: ?number=1 | ?revelation_place=Makka | ?name=fotiha
    """
    serializer_class = SuraListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = SuraFilter
    search_fields = ['name_arabic', 'name_uzbek', 'name_english', 'name_russian', 'number']
    ordering_fields = ['number', 'total_ayahs']
    ordering = ['number']

    def get_queryset(self):
        return Sura.objects.all()

    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# ─────────────────────────────────────────────
# Bitta sura  GET /api/v3/suras/<number>/
# ─────────────────────────────────────────────
@extend_schema(tags=["Suralar"])
class SuraDetailView(generics.RetrieveAPIView):
    """
    Bitta suraning barcha oyatlari bilan to'liq ma'lumoti.
    """
    serializer_class = SuraDetailSerializer
    lookup_field = 'number'

    def get_queryset(self):
        return Sura.objects.prefetch_related('ayahs__author')

    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


# ─────────────────────────────────────────────
# Bitta oyat  GET /api/v3/suras/<sura_number>/ayahs/<ayah_number>/
# ─────────────────────────────────────────────
@extend_schema(tags=["Oyatlar"])
class AyahDetailView(generics.RetrieveAPIView):
    """
    Bitta oyatning to'liq ma'lumoti.
    """
    serializer_class = AyahSerializer

    def get_object(self):
        return generics.get_object_or_404(
            Ayah.objects.select_related('sura', 'author'),
            sura__number=self.kwargs['sura_number'],
            number=self.kwargs['ayah_number']
        )

    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


# ─────────────────────────────────────────────
# Oyatlar ro'yxati  GET /api/v3/ayahs/
# ─────────────────────────────────────────────
@extend_schema(tags=["Oyatlar"])
class AyahListView(generics.ListAPIView):
    """
    Oyatlarni filter qilish.
    Filter: ?sura=1 | ?number=7 | ?search=bismillah
    """
    serializer_class = AyahSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = AyahFilter
    search_fields = ['text_arabic', 'text_uzbek', 'text_english', 'text_russian']

    def get_queryset(self):
        return Ayah.objects.select_related('sura', 'author').order_by('sura__number', 'number')

    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# ─────────────────────────────────────────────
# Mualliflar  GET /api/v3/authors/
# ─────────────────────────────────────────────
@extend_schema(tags=["Mualliflar"])
class AuthorListView(generics.ListAPIView):
    """
    Barcha mualliflar/qorilar ro'yxati.
    Filter: ?language=uz | ?language=ar
    """
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['language']
    search_fields = ['full_name']

    def get_queryset(self):
        return Author.objects.all()

    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# ─────────────────────────────────────────────
# Qur'on kitoblari  GET /api/v3/books/
# ─────────────────────────────────────────────
@extend_schema(tags=["Kitoblar"])
class QuranBookListView(generics.ListAPIView):
    """
    Barcha tillardagi Qur'on PDF kitoblari.
    Filter: ?language=uz | ?language=ar | ?language=en | ?language=ru
    """
    serializer_class = QuranBookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['language', 'can_read_online']

    def get_queryset(self):
        return QuranBook.objects.all()

    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
