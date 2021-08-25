# Generated by Django 3.1.6 on 2021-08-24 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_seance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seance',
            options={'verbose_name': 'Сеанс', 'verbose_name_plural': 'Сеанс'},
        ),
        migrations.AddField(
            model_name='seance',
            name='FilmName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.film'),
        ),
    ]
