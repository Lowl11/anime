# Generated by Django 3.0.5 on 2020-06-09 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0014_auto_20200416_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='tags',
            field=models.CharField(max_length=1000, null=True, verbose_name='Поисковые теги'),
        ),
    ]
