from django.db import models
from django.urls import reverse
import random
import string
from datetime import datetime
# Create your models here.


class SaveUrlShortened(models.Model):

    def generate_short_url(self):
        random_digits_for_ur = ''.join(random.choices(
            f'{string.ascii_lowercase}{string.ascii_uppercase}{string.digits}', k=8))

        return f'{random_digits_for_ur}'

    user = models.CharField(max_length=200, default='')
    original_url = models.CharField(max_length=800, default='', blank=False)
    title = models.CharField(max_length=200, default='', blank=True)
    short_url = models.SlugField(max_length=100, unique=True, blank=True)
    icon = models.CharField(
        max_length=400, default='../media/default/icon_broken.webp', editable=True)
    clicks = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Url Shorts'
        db_table = 'urls_shorts'

    def save(self, *args, **kwargs):
        if not self.short_url:
            new_url_short = self.generate_short_url()

            if SaveUrlShortened.objects.filter(short_url=new_url_short).exists() == False:
                self.short_url = new_url_short
                super().save(*args, **kwargs)

            else:
                print('antes del while')
                while SaveUrlShortened.objects.filter(short_url=self.short_url).exists():
                    self.short_url = self.generate_short_url()
                super().save(*args, **kwargs)

        else:

            if self.short_url == self.short_url:
                self.short_url = self.short_url
                super().save(*args, **kwargs)

                self.short_url = f'{self.short_url}'
                super().save(*args, **kwargs)

    def __str__(self):
        return 'The url short has been created'

    def redirect_original_url(self):
        return reverse('redirect_urls', args=[self.short_url])
