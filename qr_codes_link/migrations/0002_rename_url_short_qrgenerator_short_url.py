# Generated by Django 5.0.2 on 2024-03-31 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qr_codes_link', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qrgenerator',
            old_name='url_short',
            new_name='short_url',
        ),
    ]
