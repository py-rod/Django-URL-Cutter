from django.db import models
import string
import random
from django.urls import reverse
# Create your models here.


class ModelQR(models.Model):

    def generate_short_url(self):
        random_digits_for_ur = ''.join(random.choices(
            f'{string.ascii_lowercase}{string.ascii_uppercase}{string.digits}', k=9))

        return f'{random_digits_for_ur}'

    user = models.CharField(max_length=200, default='')
    original_url = models.CharField(max_length=800, default='', blank=False)
    title = models.CharField(max_length=200, blank=True, default='')
    short_url = models.SlugField(max_length=100, unique=True, blank=True)
    bg_color_qr = models.CharField(
        max_length=200, default='#FFFFFF', blank=True)
    color_qr = models.CharField(
        max_length=200, default='#00CA7D', blank=True)
    border_color_qr = models.CharField(
        max_length=200, default='#FFFFFF', blank=True)
    border_qr = models.IntegerField(default=0)
    scans = models.PositiveIntegerField(default=0)
    type_app = models.CharField(max_length=100, default='', blank=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        verbose_name_plural = 'QR Codes Links'
        db_table = 'qr_code_links'

    def save(self, *args, **kwargs):
        if not self.short_url:
            new_url_short = self.generate_short_url()

            if ModelQR.objects.filter(short_url=new_url_short).exists() == False:
                self.short_url = new_url_short
                super().save(*args, **kwargs)

            else:
                while ModelQR.objects.filter(short_url=self.short_url).exists():
                    self.short_url = self.generate_short_url()
                super().save(*args, **kwargs)

        else:

            if self.short_url == self.short_url:
                self.short_url = self.short_url
                super().save(*args, **kwargs)

                self.short_url = f'{self.short_url}'
                super().save(*args, **kwargs)

    def __str__(self):
        return f'The QR Code {self.title} has been created'

    def redirect_original_qr_link(self):
        return reverse('redirect_qr', args=[self.short_url])
