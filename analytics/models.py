from django.db import models

# Create your models here.


class UrlAnalytics(models.Model):
    id_short_url = models.CharField(
        max_length=500, default='', unique=False, blank=False)
    creator = models.CharField(max_length=200, default='', blank=False)
    is_mobile = models.BooleanField(default=False)
    is_tablet = models.BooleanField(default=False)
    is_pc = models.BooleanField(default=False)
    is_touch_capable = models.BooleanField(default=False)
    is_bot = models.BooleanField(default=False)
    browser = models.CharField(max_length=200, default='', blank=True)
    mobile_system = models.CharField(max_length=100, default='', blank=True)
    device = models.CharField(max_length=100, default='', blank=True)
    created = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        verbose_name_plural = 'URLAnalytics'
        db_table = 'URLAnalytics'

    def __str__(self) -> str:
        return f'Analytic data has been created to {self.id_short_url}'


class QRAnalytics(models.Model):
    id_short_url = models.CharField(
        max_length=500, default='', unique=False, blank=False)
    creator = models.CharField(max_length=200, default='', blank=False)
    is_mobile = models.BooleanField(default=False)
    is_tablet = models.BooleanField(default=False)
    is_pc = models.BooleanField(default=False)
    is_touch_capable = models.BooleanField(default=False)
    is_bot = models.BooleanField(default=False)
    browser = models.CharField(max_length=200, default='', blank=True)
    mobile_system = models.CharField(max_length=100, default='', blank=True)
    device = models.CharField(max_length=100, default='', blank=True)
    created = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        verbose_name_plural = 'QRAnalytics'
        db_table = 'QRAnalytics'

    def __str__(self) -> str:
        return f'Analytic data has been created to {self.id_short_url}'
