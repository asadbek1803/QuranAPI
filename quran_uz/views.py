from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SuraSerializer

from .models import Sura, Oyat, Author


# Create your views here.

# class SuraList(generics.RetrieveAPIView):
#     queryset = Sura.objects.all()
#     serializer_class = SuraSerializer

# class SuraList(APIView):
#     def get(self, request, sura_name):
#         sura = Sura.objects.get(name=sura_name)
#
#
#         serializer = SuraSerializer(sura)
#         # print(serializer.data)
#         return Response(serializer.data)

class SuraList(generics.RetrieveAPIView):
    serializer_class = SuraSerializer
    queryset = Sura.objects.all() #Quronni /api/v2/uz/quran/1/ bu quronning birinchi surasini ko'rsatib beradi





