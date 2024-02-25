from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from quran.models import Quran, Sura
from quran.serializers import SuraSerializer
from rest_framework.response import Response

# Create your views here.

def read_quran(request):

    data = {
        'quran': Quran.objects.all()
    }

    return redirect('/media/quran/books/Quran.pdf')


# class SuraApiView(APIView):
#     def get(self, request, name, sura_number=None):
#         sura_number = None
#         if sura_number==None:
#             sura = get_object_or_404(Sura, name=name)
#
#             sura_serializer = SuraSerializer(sura)
#         else:
#             sura = get_object_or_404(Sura, name=name, sura_number=sura_number)
#             sura_serializer = SuraSerializer(sura)
#
#         return Response(sura_serializer.data)
class SuraList(ListAPIView):

    queryset = Sura.objects.all()
    serializer_class = SuraSerializer

