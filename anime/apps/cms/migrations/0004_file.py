# Generated by Django 3.0.5 on 2020-05-05 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_cmsnavigationlink_glyph_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=999)),
            ],
        ),
    ]