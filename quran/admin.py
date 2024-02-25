from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.
from .models import Author, Sura, Oyat, Quran
@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    list_display = ('id', 'full_name', 't_yil', 'profile_image', 'about')
    list_display_links = ('id', 'full_name')
    list_editable = ('profile_image', )
    search_fields = ('id', 'full_name')
admin.site.register(Sura)



@admin.register(Oyat)
class OyatAdmin(ModelAdmin):
    list_display = ('id', 'sura', 'oyat_number', 'tarjima', 'audio', 'author')

    list_editable = ('oyat_number', )
    search_fields = ('id', 'oyat_number', )
    list_filter = ('oyat_number', )

@admin.register(Quran)
class QuranAdmin(ModelAdmin):
    list_display = ('id', 'full_name', 'pdf', 'online_read')
    list_display_links = ('id', 'full_name', )
    list_editable = ('online_read', )
    search_fields = ('id', )
    list_filter = ('id', )

