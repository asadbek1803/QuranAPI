from rest_framework import serializers
from .models import Author, Sura, Ayah, QuranBook


class AuthorSerializer(serializers.ModelSerializer):
    language_display = serializers.CharField(
        source='get_language_display', read_only=True
    )

    class Meta:
        model = Author
        fields = ('id', 'full_name', 'profile_image', 'birth_year', 'about', 'language', 'language_display')


class AyahSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.full_name', read_only=True, default=None)

    class Meta:
        model = Ayah
        fields = (
            'id', 'number',
            'text_arabic', 'text_uzbek', 'text_russian', 'text_english',
            'audio_arabic', 'audio_uzbek',
            'author_name',
        )


class SuraListSerializer(serializers.ModelSerializer):
    """Qisqacha — barcha suralar ro'yxati uchun"""
    class Meta:
        model = Sura
        fields = ('id', 'number', 'name_arabic', 'name_uzbek', 'name_english', 'name_russian', 'total_ayahs', 'revelation_place')


class SuraDetailSerializer(serializers.ModelSerializer):
    """To'liq — bitta suraning barcha oyatlari bilan"""
    ayahs = AyahSerializer(many=True, read_only=True)

    class Meta:
        model = Sura
        fields = ('id', 'number', 'name_arabic', 'name_uzbek', 'name_english', 'name_russian', 'total_ayahs', 'revelation_place', 'ayahs')


class QuranBookSerializer(serializers.ModelSerializer):
    language_display = serializers.CharField(source='get_language_display', read_only=True)

    class Meta:
        model = QuranBook
        fields = ('id', 'title', 'language', 'language_display', 'pdf', 'can_read_online', 'uploaded_at')
