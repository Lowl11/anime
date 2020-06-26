# Generated by Django 3.0.5 on 2020-06-26 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a_auth', '0006_auto_20200418_1308'),
        ('watch', '0016_auto_20200609_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Anime')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_auth.Viewer')),
            ],
            options={
                'verbose_name': 'Комментарий под аниме',
                'verbose_name_plural': 'Комментарии под аниме',
            },
        ),
    ]
