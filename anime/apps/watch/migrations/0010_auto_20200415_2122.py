# Generated by Django 3.0.5 on 2020-04-15 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0009_genre_anime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Anime'),
        ),
    ]
