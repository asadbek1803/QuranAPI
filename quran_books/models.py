from django.db import models

# Create your models here.
class Quran(models.Model):
    language = (
        ('en', 'English'),
        ('uz', 'Uzbek'),
        ('ru', 'Russian'),
        ('ar', 'Arabic')
    )
    full_name = models.CharField(max_length=150, default="Quran")
    pdf = models.FileField(upload_to='quran/books/')
    lang = models.CharField(max_length=35, choices=language, null=True, blank=True)
    online_read = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return self.full_name

    def get_obolute_url(self):
        return "/" + str(self.id) + "/"

    class Meta:
        verbose_name = "Quran"
        verbose_name_plural = "Quran"