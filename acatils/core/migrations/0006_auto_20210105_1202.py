# Generated by Django 3.1.5 on 2021-01-05 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210105_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='description',
            field=models.TextField(blank=True, max_length=700, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=1000, verbose_name='Slug'),
        ),
    ]