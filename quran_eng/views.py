from django.http import Http404, JsonResponse
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SuraSerializer, OyatForSuraSerializer, SuraForOyatSerializer

from .models import Sura, Oyat, Author


class SuraList(generics.RetrieveAPIView):

    serializer_class = SuraSerializer

    #Quronni /api/v2/uz/quran/1/ bu quronning birinchi surasini ko'rsatib beradi
    def get_queryset(self, *args, **kwargs):


            return Sura.objects.filter(id=self.kwargs['pk'])



class SuraDetail(generics.RetrieveAPIView):
    serializer_class = OyatForSuraSerializer

    def get_object(self):
        sura_id = self.kwargs['pk']
        oyat_number = self.kwargs['oyat_number']

        sura = get_object_or_404(Sura, pk=sura_id)
        oyat = sura.oyat.get(oyat_number=oyat_number)
        return oyat
