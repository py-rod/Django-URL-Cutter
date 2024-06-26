# Generated by Django 5.0.2 on 2024-04-02 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_codes_link', '0007_qrgenerator_color_qr'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrgenerator',
            name='bg_color_qr',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='qrgenerator',
            name='border_qr',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='qrgenerator',
            name='zone_color_qr',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
