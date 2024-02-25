from django.db import models

# Create your models here.
class Quran(models.Model):
    full_name = models.CharField(max_length=150, default="Quran")
    pdf = models.FileField(upload_to='quran/books/')
    online_read = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Quran"
        verbose_name_plural = "Quran"


class Author(models.Model):
    full_name = models.CharField(max_length=150)
    profile_image = models.ImageField(upload_to='quran/author/image/')
    t_yil = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return self.full_name


    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authorlar"

class Oyat(models.Model):
    sura = models.CharField(max_length=150)
    oyat_number = models.BigIntegerField(default=0)
    tarjima = models.TextField(default="Tarjimasi")
    audio = models.FileField(upload_to='quran/audio/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.sura

    class Meta:
        verbose_name = "Oyat"
        verbose_name_plural = "Oyatlar"

class Sura(models.Model):
    name = models.CharField(max_length=200)
    jami_oyat = models.IntegerField(default=0)
    oyat = models.ManyToManyField(Oyat, related_name="oyat")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sura"
        verbose_name_plural = "Suralar"