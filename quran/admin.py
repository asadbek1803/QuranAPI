from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin

from .models import Author, Sura, Ayah, QuranBook
from .resources import AuthorResource, SuraResource, AyahResource, QuranBookResource


# ─────────────────────────────────────────────
# Admin sayt sarlavhasi va ko'rinishi
# ─────────────────────────────────────────────
admin.site.site_header = "🕌 Quran API — Admin Panel"
admin.site.site_title = "Quran Admin"
admin.site.index_title = "Bosh sahifa"


# ─────────────────────────────────────────────
# Muallif (Author) Admin
# ─────────────────────────────────────────────
@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    resource_class = AuthorResource

    list_display = ('id', 'full_name', 'language_badge', 'birth_year', 'avatar_preview')
    list_display_links = ('id', 'full_name')
    list_filter = ('language',)
    search_fields = ('full_name', 'about')
    ordering = ('language', 'full_name')

    fieldsets = (
        ("Asosiy ma'lumot", {
            'fields': ('full_name', 'language', 'birth_year', 'about')
        }),
        ("Rasm", {
            'fields': ('profile_image',),
            'classes': ('collapse',),
        }),
    )

    @admin.display(description="Til", ordering='language')
    def language_badge(self, obj):
        colors = {'uz': '#1e7e34', 'ar': '#856404', 'ru': '#155724', 'en': '#004085'}
        labels = {'uz': "🇺🇿 O'zbek", 'ar': '🇸🇦 Arab', 'ru': '🇷🇺 Rus', 'en': '🇬🇧 Ingliz'}
        color = colors.get(obj.language, '#666')
        label = labels.get(obj.language, obj.language)
        return format_html(
            '<span style="background:{};color:#fff;padding:3px 8px;border-radius:4px;font-size:12px">{}</span>',
            color, label
        )

    @admin.display(description="Rasm")
    def avatar_preview(self, obj):
        if obj.profile_image:
            return format_html(
                '<img src="{}" width="40" height="40" style="border-radius:50%;object-fit:cover" />',
                obj.profile_image.url
            )
        return "—"


# ─────────────────────────────────────────────
# Oyat Inline — Sura ichida ko'rish
# ─────────────────────────────────────────────
class AyahInline(admin.TabularInline):
    model = Ayah
    extra = 1
    fields = ('number', 'text_arabic', 'text_uzbek', 'text_russian', 'text_english')
    ordering = ('number',)
    show_change_link = True


# ─────────────────────────────────────────────
# Sura Admin
# ─────────────────────────────────────────────
@admin.register(Sura)
class SuraAdmin(ImportExportModelAdmin):
    resource_class = SuraResource

    list_display = ('number', 'name_arabic', 'name_uzbek', 'total_ayahs', 'revelation_badge')
    list_display_links = ('number', 'name_arabic')
    search_fields = ('name_arabic', 'name_uzbek', 'name_english', 'number')
    list_filter = ('revelation_place',)
    ordering = ('number',)
    list_per_page = 30

    fieldsets = (
        ("Asosiy", {
            'fields': ('number', 'total_ayahs', 'revelation_place')
        }),
        ("Suraning nomlari", {
            'fields': ('name_arabic', 'name_uzbek', 'name_english', 'name_russian'),
        }),
    )

    inlines = [AyahInline]

    @admin.display(description="Nozil bo'lgan joy", ordering='revelation_place')
    def revelation_badge(self, obj):
        if not obj.revelation_place:
            return "—"
        color = '#856404' if 'Makka' in (obj.revelation_place or '') else '#155724'
        return format_html(
            '<span style="background:{};color:#fff;padding:3px 8px;border-radius:4px;font-size:12px">📍 {}</span>',
            color, obj.revelation_place
        )


# ─────────────────────────────────────────────
# Oyat Admin
# ─────────────────────────────────────────────
@admin.register(Ayah)
class AyahAdmin(ImportExportModelAdmin):
    resource_class = AyahResource

    list_display = ('id', 'sura_link', 'number', 'short_arabic', 'short_uzbek', 'author')
    list_display_links = ('id', 'number')
    list_filter = ('sura', 'author')
    search_fields = ('text_arabic', 'text_uzbek', 'text_russian', 'text_english', 'number')
    ordering = ('sura__number', 'number')
    autocomplete_fields = ('sura', 'author')
    list_per_page = 50
    list_select_related = ('sura', 'author')

    fieldsets = (
        ("Joylashuv", {
            'fields': ('sura', 'number', 'author')
        }),
        ("Matnlar", {
            'fields': ('text_arabic', 'text_uzbek', 'text_russian', 'text_english'),
        }),
        ("Audio fayllar", {
            'fields': ('audio_arabic', 'audio_uzbek'),
            'classes': ('collapse',),
        }),
    )

    @admin.display(description="Sura", ordering='sura__number')
    def sura_link(self, obj):
        return format_html(
            '<a href="../sura/{}/change/">{}</a>',
            obj.sura_id, str(obj.sura)
        )

    @admin.display(description="Arabcha matn")
    def short_arabic(self, obj):
        return (obj.text_arabic[:60] + '…') if len(obj.text_arabic) > 60 else obj.text_arabic

    @admin.display(description="O'zbekcha tarjima")
    def short_uzbek(self, obj):
        if not obj.text_uzbek:
            return format_html('<span style="color:#999">—</span>')
        return (obj.text_uzbek[:60] + '…') if len(obj.text_uzbek) > 60 else obj.text_uzbek


# ─────────────────────────────────────────────
# Qur'on kitoblari Admin
# ─────────────────────────────────────────────
@admin.register(QuranBook)
class QuranBookAdmin(ImportExportModelAdmin):
    resource_class = QuranBookResource

    list_display = ('id', 'title', 'language_badge', 'can_read_online', 'pdf_link', 'uploaded_at')
    list_display_links = ('id', 'title')
    list_filter = ('language', 'can_read_online')
    search_fields = ('title',)
    ordering = ('language',)

    @admin.display(description="Til", ordering='language')
    def language_badge(self, obj):
        colors = {'uz': '#1e7e34', 'ar': '#856404', 'ru': '#155724', 'en': '#004085'}
        labels = {'uz': "🇺🇿 O'zbek", 'ar': '🇸🇦 Arab', 'ru': '🇷🇺 Rus', 'en': '🇬🇧 Ingliz'}
        color = colors.get(obj.language, '#666')
        label = labels.get(obj.language, obj.language)
        return format_html(
            '<span style="background:{};color:#fff;padding:3px 8px;border-radius:4px;font-size:12px">{}</span>',
            color, label
        )

    @admin.display(description="PDF")
    def pdf_link(self, obj):
        if obj.pdf:
            return format_html(
                '<a href="{}" target="_blank" style="color:#0d6efd">📄 Ochish</a>',
                obj.pdf.url
            )
        return "—"
