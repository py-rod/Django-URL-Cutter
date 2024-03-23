from django.contrib import admin
from .models import QRGenerator

# Register your models here.


@admin.register(QRGenerator)
class QRGeneratorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'url_short', 'title')
    list_display_links = ('id', 'user', 'url_short', 'title')
    list_per_page = 20
    search_fields = ('id', 'url_short', 'title')
