from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Sura, Ayah, Author, QuranBook


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author
        fields = ('id', 'full_name', 'birth_year', 'about', 'language')
        export_order = ('id', 'full_name', 'language', 'birth_year', 'about')
        import_id_fields = ('id',)


class SuraResource(resources.ModelResource):
    class Meta:
        model = Sura
        fields = (
            'id', 'number', 'name_arabic', 'name_uzbek',
            'name_english', 'name_russian', 'total_ayahs', 'revelation_place'
        )
        export_order = (
            'id', 'number', 'name_arabic', 'name_uzbek',
            'name_english', 'name_russian', 'total_ayahs', 'revelation_place'
        )
        import_id_fields = ('number',)


class AyahResource(resources.ModelResource):
    sura_number = fields.Field(
        column_name='sura_number',
        attribute='sura',
        widget=ForeignKeyWidget(Sura, field='number')
    )

    class Meta:
        model = Ayah
        fields = (
            'id', 'sura_number', 'number',
            'text_arabic', 'text_uzbek', 'text_russian', 'text_english',
        )
        export_order = (
            'id', 'sura_number', 'number',
            'text_arabic', 'text_uzbek', 'text_russian', 'text_english',
        )
        import_id_fields = ('sura_number', 'number')


class QuranBookResource(resources.ModelResource):
    class Meta:
        model = QuranBook
        fields = ('id', 'title', 'language', 'can_read_online', 'uploaded_at')
        export_order = ('id', 'title', 'language', 'can_read_online', 'uploaded_at')
        import_id_fields = ('id',)
