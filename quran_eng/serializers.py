from rest_framework import serializers
from .models import Sura, Author, Oyat


class AuthorForOyat(serializers.ModelSerializer):
    class Meta:
        model = Author
        ref_name = 'AuthorEnglish'
        fields = ('full_name', 'profile_image')




class OyatForSuraSerializer(serializers.ModelSerializer):
    author = AuthorForOyat()
    class Meta:
        audio = Oyat.audio
        model = Oyat
        fields = ('oyat_number', 'tarjima', 'audio', 'author')


class SuraSerializer(serializers.ModelSerializer):
    oyat = OyatForSuraSerializer(many=True)
    class Meta:
        model = Sura
        ref_name = 'SuraEnglish'
        fields = ('name', 'jami_oyat', 'oyat', 'written')

class SuraForOyatSerializer(serializers.ModelSerializer):
    oyat = OyatForSuraSerializer(many=True)
    class Meta:
        model = Sura
        ref_name = 'SuraForOyatEnglish'
        fields = ('name', 'jami_oyat', 'oyat', 'written')
