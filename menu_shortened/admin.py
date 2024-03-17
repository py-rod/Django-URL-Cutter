from django.contrib import admin
from .models import SaveUrlShortened
# Register your models here.


@admin.register(SaveUrlShortened)
class SaveUrlShortenedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'short_url',  'created')
    list_display_links = ('id', 'user', 'title', 'short_url')
    list_per_page = 20
    search_fields = ('id', 'short_url', 'title')
