from rest_framework import serializers
from .models import Sura, Author, Oyat


class AuthorForOyat(serializers.ModelSerializer):
    class Meta:
        model = Author
        ref_name = 'AuthorRussian'
        fields = ('full_name', 'profile_image')




class OyatForSuraSerializer(serializers.ModelSerializer):
    author = AuthorForOyat()
    class Meta:
        audio = Oyat.audio
        model = Oyat
        ref_name = 'OyatRussian'
        fields = ('oyat_number', 'tarjima', 'audio', 'author')


class SuraSerializer(serializers.ModelSerializer):
    oyat = OyatForSuraSerializer(many=True)
    class Meta:
        model = Sura
        ref_name = 'SuraRussian'
        fields = ('name', 'jami_oyat', 'oyat', 'written')

class SuraForOyatSerializer(serializers.ModelSerializer):
    oyat = OyatForSuraSerializer(many=True)
    class Meta:
        model = Sura
        ref_name = 'SuraForOyatRussian'
        fields = ('name', 'jami_oyat', 'oyat', 'written')
