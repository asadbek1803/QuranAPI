from rest_framework import serializers
from .models import Sura, Author, Oyat


class AuthorForOyat(serializers.ModelSerializer):
    class Meta:
        model = Author
        ref_name = 'AuthorUzbek'
        fields = ('full_name', 'profile_image')




class OyatForSuraSerializer(serializers.ModelSerializer):
    author = AuthorForOyat()
    class Meta:
        audio = Oyat.audio
        model = Oyat
        ref_name = 'OyatUzbek'
        fields = ('oyat_number', 'tarjima', 'audio', 'author')


class SuraSerializer(serializers.ModelSerializer):
    oyat = OyatForSuraSerializer(many=True)
    class Meta:
        model = Sura
        ref_name = 'SuraUzbek'
        fields = ('name', 'jami_oyat', 'oyat', 'yozilgan_joyi')

class SuraForOyatSerializer(serializers.ModelSerializer):
    oyat = OyatForSuraSerializer(many=True)
    class Meta:
        model = Sura
        ref_name = 'SuraForOyatUzbek'
        fields = ('name', 'jami_oyat', 'oyat', 'yozilgan_joyi')


