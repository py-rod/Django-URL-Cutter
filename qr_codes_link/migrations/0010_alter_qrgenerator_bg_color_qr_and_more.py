# Generated by Django 5.0.2 on 2024-04-02 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_codes_link', '0009_remove_qrgenerator_zone_color_qr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrgenerator',
            name='bg_color_qr',
            field=models.CharField(blank=True, default='#000000', max_length=200),
        ),
        migrations.AlterField(
            model_name='qrgenerator',
            name='color_qr',
            field=models.CharField(blank=True, default='#FFFFFF', max_length=200),
        ),
    ]
