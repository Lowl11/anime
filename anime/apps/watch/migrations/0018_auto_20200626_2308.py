# Generated by Django 3.0.5 on 2020-06-26 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_auth', '0006_auto_20200418_1308'),
        ('watch', '0017_animecomments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AnimeComments',
            new_name='AnimeComment',
        ),
    ]
