# Generated by Django 3.1.5 on 2021-01-16 00:46

import core.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210115_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img',
            field=stdimage.models.StdImageField(blank=True, upload_to=core.models.get_file_path, verbose_name='Imagem'),
        ),
    ]
