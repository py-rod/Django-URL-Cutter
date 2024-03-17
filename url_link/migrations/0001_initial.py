# Generated by Django 5.0.2 on 2024-03-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaveUrlShortened',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=200)),
                ('original_url', models.CharField(default='', max_length=800)),
                ('title', models.CharField(blank=True, default='', max_length=200)),
                ('short_url', models.CharField(blank=True, max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Url Shorts',
                'db_table': 'urls_shorts',
            },
        ),
    ]
