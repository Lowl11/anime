# Generated by Django 3.0.5 on 2020-04-16 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0012_auto_20200415_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constantgenre',
            name='order_number',
            field=models.IntegerField(unique=True, verbose_name='Порядковый номер'),
        ),
    ]
