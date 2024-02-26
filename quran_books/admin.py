from django.contrib import admin
from django.contrib.admin import ModelAdmin

from quran_books.models import Quran


# Register your models here.
@admin.register(Quran)
class QuranAdmin(ModelAdmin):
    list_display = ('id', 'full_name', 'pdf', 'online_read')
    list_display_links = ('id', 'full_name', )
    list_editable = ('online_read', )
    search_fields = ('id', )
    list_filter = ('id', )
