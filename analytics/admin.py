from django.contrib import admin
from .models import UrlAnalytics, QRAnalytics
# Register your models here.


@admin.register(UrlAnalytics)
class UrlAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_short_url', 'creator', 'created')
    list_display_links = ('id', 'id_short_url')
    list_filter = ('is_mobile', 'is_tablet', 'is_pc', 'is_touch_capable',
                   'is_bot', 'browser', 'mobile_system', 'device')
    list_per_page = 20
    search_fields = ('id', 'id_short_url')


@admin.register(QRAnalytics)
class UrlAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_short_url', 'creator', 'created')
    list_display_links = ('id', 'id_short_url')
    list_filter = ('is_mobile', 'is_tablet', 'is_pc', 'is_touch_capable',
                   'is_bot', 'browser', 'mobile_system', 'device')
    list_per_page = 20
    search_fields = ('id', 'id_short_url')
