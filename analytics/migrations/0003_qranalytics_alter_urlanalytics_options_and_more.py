# Generated by Django 5.0.2 on 2024-04-10 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_alter_urlanalytics_id_short_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='QRAnalytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('id_short_url', models.CharField(default='', max_length=500)),
                ('is_mobile', models.BooleanField(default=False)),
                ('is_tablet', models.BooleanField(default=False)),
                ('is_pc', models.BooleanField(default=False)),
                ('is_touch_capable', models.BooleanField(default=False)),
                ('is_bot', models.BooleanField(default=False)),
                ('browser', models.CharField(blank=True, default='', max_length=200)),
                ('mobile_system', models.CharField(blank=True, default='', max_length=100)),
                ('device', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'QRAnalytics',
                'db_table': 'QRAnalytics',
            },
        ),
        migrations.AlterModelOptions(
            name='urlanalytics',
            options={'verbose_name_plural': 'URLAnalytics'},
        ),
        migrations.AlterModelTable(
            name='urlanalytics',
            table='URLAnalytics',
        ),
    ]