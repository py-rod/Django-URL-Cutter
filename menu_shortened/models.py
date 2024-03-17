from typing import Iterable
from django.db import models
import hashlib
import random
import string
# Create your models here.


class SaveUrlShortened(models.Model):

    def generate_short_url(self, protocol):
        random_digits_for_ur = ''.join(random.choices(
            f'{string.ascii_lowercase}{string.ascii_uppercase}{string.digits}', k=8))

        return f'{protocol}://URLTrim.ly/{random_digits_for_ur}'

    user = models.CharField(max_length=200, default='')
    original_url = models.CharField(max_length=800, default='', blank=False)
    title = models.CharField(max_length=200, default='', blank=True)
    short_url = models.CharField(max_length=100, unique=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Url Shorts'
        db_table = 'urls_shorts'

    def save(self, protocol=None, *args, **kwargs):
        if not self.short_url:
            protocol = protocol or 'https'
            new_url_short = self.generate_short_url(protocol)
            print('Esta vacio y esto es en modelo')
            if SaveUrlShortened.objects.filter(short_url=new_url_short).exists() == False:
                print('No existe esta url corta en la base de datos')
                self.short_url = new_url_short
                super().save(*args, **kwargs)

            else:
                print('antes del while')
                while SaveUrlShortened.objects.filter(short_url=self.short_url).exists():
                    print('Corriendo el bucle por repetido')
                    self.short_url = self.generate_short_url(protocol)
                super().save(*args, **kwargs)

        else:
            print('No esta vacio')
            if not SaveUrlShortened.objects.filter(short_url=self.short_url).exists():
                print('dsf')
                protocol = protocol or 'https'
                self.short_url = f'{protocol}://URLTrim.ly/{self.short_url}'
                super().save(*args, **kwargs)

    def __str__(self):
        return 'The url short has been created'
