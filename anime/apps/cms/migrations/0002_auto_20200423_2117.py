# Generated by Django 3.0.5 on 2020-04-23 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CmsNavigationLinks',
            new_name='CmsNavigationLink',
        ),
    ]
