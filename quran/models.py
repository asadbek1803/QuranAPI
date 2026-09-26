from django.db import models
from django.utils.translation import gettext_lazy as _


class Language(models.TextChoices):
    UZBEK = 'uz', _("O'zbekcha")
    ARABIC = 'ar', _("Arabcha")
    RUSSIAN = 'ru', _("Ruscha")
    ENGLISH = 'en', _("Inglizcha")


class Author(models.Model):
    """
    Tarjimon yoki qori haqida ma'lumot.
    """
    full_name = models.CharField(max_length=150, verbose_name="To'liq ismi")
    profile_image = models.ImageField(
        upload_to='quran/authors/', verbose_name="Rasm", blank=True, null=True
    )
    birth_year = models.CharField(max_length=100, verbose_name="Tug'ilgan yil", blank=True)
    about = models.TextField(verbose_name="Haqida", blank=True)
    language = models.CharField(
        max_length=5, choices=Language.choices,
        verbose_name="Til", default=Language.UZBEK
    )

    def __str__(self):
        return f"{self.full_name} ({self.get_language_display()})"

    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"
        ordering = ['full_name']
        indexes = [
            models.Index(fields=['language']),
        ]


class Sura(models.Model):
    """
    Qur'on surasi.
    """
    number = models.PositiveIntegerField(
        unique=True, verbose_name="Sura raqami", db_index=True
    )
    name_arabic = models.CharField(max_length=200, verbose_name="Arabcha nomi")
    name_uzbek = models.CharField(max_length=200, verbose_name="O'zbekcha nomi", blank=True)
    name_english = models.CharField(max_length=200, verbose_name="Inglizcha nomi", blank=True)
    name_russian = models.CharField(max_length=200, verbose_name="Ruscha nomi", blank=True)
    total_ayahs = models.PositiveIntegerField(default=0, verbose_name="Jami oyatlar")
    revelation_place = models.CharField(
        max_length=100, verbose_name="Nozil bo'lgan joy",
        blank=True, null=True,
        help_text="Makka yoki Madina"
    )

    def __str__(self):
        return f"{self.number}. {self.name_arabic}"

    class Meta:
        verbose_name = "Sura"
        verbose_name_plural = "Suralar"
        ordering = ['number']
        indexes = [
            models.Index(fields=['number']),
            models.Index(fields=['name_arabic']),
        ]


class Ayah(models.Model):
    """
    Qur'on oyati — bir sura ichidagi bitta oyat, ko'p tilda.
    """
    sura = models.ForeignKey(
        Sura, on_delete=models.CASCADE,
        related_name='ayahs', verbose_name="Sura"
    )
    number = models.PositiveIntegerField(verbose_name="Oyat raqami", db_index=True)
    text_arabic = models.TextField(verbose_name="Arabcha matn")
    text_uzbek = models.TextField(verbose_name="O'zbekcha tarjima", blank=True)
    text_russian = models.TextField(verbose_name="Ruscha tarjima", blank=True)
    text_english = models.TextField(verbose_name="Inglizcha tarjima", blank=True)
    audio_arabic = models.FileField(
        upload_to='quran/audio/arabic/', verbose_name="Arabcha audio",
        blank=True, null=True
    )
    audio_uzbek = models.FileField(
        upload_to='quran/audio/uzbek/', verbose_name="O'zbekcha audio",
        blank=True, null=True
    )
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='ayahs', verbose_name="Tarjimon"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sura.name_arabic} - {self.number}-oyat"

    class Meta:
        verbose_name = "Oyat"
        verbose_name_plural = "Oyatlar"
        ordering = ['sura__number', 'number']
        unique_together = [('sura', 'number')]
        indexes = [
            models.Index(fields=['sura', 'number']),
            models.Index(fields=['number']),
        ]


class QuranBook(models.Model):
    """
    Qur'on PDF kitoblari turli tillarda.
    """
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    language = models.CharField(
        max_length=5, choices=Language.choices, verbose_name="Til"
    )
    pdf = models.FileField(upload_to='quran/books/', verbose_name="PDF fayl")
    can_read_online = models.BooleanField(
        default=False, verbose_name="Online o'qish mumkin"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_language_display()})"

    class Meta:
        verbose_name = "Qur'on kitobi"
        verbose_name_plural = "Qur'on kitoblari"
        ordering = ['language']
        indexes = [
            models.Index(fields=['language']),
        ]
