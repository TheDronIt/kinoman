# Generated by Django 3.1.6 on 2021-08-25 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20210824_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='Trailer',
            field=models.FileField(blank=True, null=True, upload_to='videos/', verbose_name='Трейлер'),
        ),
    ]
