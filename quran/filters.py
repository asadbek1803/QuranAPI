import django_filters
from .models import Sura, Ayah


class SuraFilter(django_filters.FilterSet):
    """
    Suralarni filter qilish:
    ?number=1
    ?revelation_place=Makka
    ?name=fotiha
    """
    name = django_filters.CharFilter(method='filter_name', label="Ismi bo'yicha qidirish")
    revelation_place = django_filters.CharFilter(
        field_name='revelation_place', lookup_expr='icontains', label="Nozil bo'lgan joy"
    )

    class Meta:
        model = Sura
        fields = ['number', 'revelation_place']

    def filter_name(self, queryset, name, value):
        return queryset.filter(
            name_arabic__icontains=value
        ) | queryset.filter(
            name_uzbek__icontains=value
        ) | queryset.filter(
            name_english__icontains=value
        ) | queryset.filter(
            name_russian__icontains=value
        )


class AyahFilter(django_filters.FilterSet):
    """
    Oyatlarni filter qilish:
    ?sura=1
    ?number=7
    ?search=bismillah
    """
    search = django_filters.CharFilter(method='filter_search', label="Matn bo'yicha qidirish")

    class Meta:
        model = Ayah
        fields = ['sura', 'number']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            text_arabic__icontains=value
        ) | queryset.filter(
            text_uzbek__icontains=value
        ) | queryset.filter(
            text_english__icontains=value
        ) | queryset.filter(
            text_russian__icontains=value
        )
