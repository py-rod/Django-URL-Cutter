# Generated by Django 5.0.2 on 2024-05-05 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_link', '0011_rename_saveurlshortened_modelsaveurlshortened'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ModelSaveUrlShortened',
            new_name='ModelUrl',
        ),
    ]
