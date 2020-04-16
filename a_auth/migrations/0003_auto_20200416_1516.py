# Generated by Django 3.0.5 on 2020-04-16 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a_auth', '0002_auto_20200416_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
            },
        ),
        migrations.AddField(
            model_name='viewer',
            name='role',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='a_auth.Role'),
            preserve_default=False,
        ),
    ]
