# Generated by Django 5.0.2 on 2024-03-30 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QRGenerator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('user', models.CharField(default='', max_length=200)),
                ('title', models.CharField(blank=True, default='', max_length=200)),
                ('original_url', models.CharField(default='', max_length=500)),
                ('url_short', models.CharField(default='', max_length=300, unique=True)),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'QR Codes Images',
                'db_table': 'qr_code_images',
            },
        ),
    ]
