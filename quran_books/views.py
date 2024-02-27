from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .models import *
from .serializers import BookSerializer

def quran_uz(request):
    book_path = Quran.objects.get(id=1)



    return JsonResponse({'status': '200', 'uz': 'http://localhost:8000/media/quran/books/Quran_p76M38M.pdf'})

def quran_ru(request):

    return JsonResponse({'status': '200', 'ru': 'http://localhost:8000/media/quran/books/Holy-Quran-Russian.pdf'})

def quran_eng(request):
    return JsonResponse({'status': '200', 'eng': 'http://localhost:8000/media/quran/books/Holy-Quran-English.pdf'})

def quran_arabic(request):
    return JsonResponse({'status': '200', 'arabic': 'http://localhost:8000/media/quran/books/Holy_Quran_Full.pdf'})
