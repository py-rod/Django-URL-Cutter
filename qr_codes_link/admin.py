from django.contrib import admin
from .models import ModelQR

# Register your models here.


@admin.register(ModelQR)
class ModelQRAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'short_url', 'title')
    list_display_links = ('id', 'user', 'short_url', 'title')
    list_per_page = 20
    search_fields = ('id', 'short_url', 'title')
