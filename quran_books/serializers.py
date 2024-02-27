from rest_framework import serializers
from .models import Quran

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quran
        fields = '__all__'
