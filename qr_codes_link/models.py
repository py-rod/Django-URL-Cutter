from django.db import models
import string
import random
import os
from django.template.defaultfilters import slugify
# Create your models here.


class QRGenerator(models.Model):

    def image_upload_to(self, instance):
        if instance:
            return os.path.join('qr_images', slugify(self.user), instance)
        return None

    user = models.CharField(max_length=200, default='')
    title = models.CharField(max_length=200, blank=True, default='')
    original_url = models.CharField(max_length=500, default='', blank=False)
    url_short = models.CharField(max_length=300, default='', unique=True)
    qr_image = models.ImageField(upload_to=image_upload_to)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'QR Codes Images'
        db_table = 'qr_code_images'

    def __str__(self):
        return 'The QR Code image has been created'
