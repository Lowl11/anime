# Generated by Django 3.0.5 on 2020-04-15 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0010_auto_20200415_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstantGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название жанра')),
                ('order_number', models.IntegerField(verbose_name='Порядковый номер')),
            ],
        ),
        migrations.RemoveField(
            model_name='genre',
            name='name',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='order_number',
        ),
        migrations.AddField(
            model_name='genre',
            name='constant_genre',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='watch.ConstantGenre'),
            preserve_default=False,
        ),
    ]