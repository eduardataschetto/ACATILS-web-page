# Generated by Django 3.1.5 on 2021-01-29 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210115_2156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-created',), 'verbose_name': 'Notícia', 'verbose_name_plural': 'Notícias'},
        ),
    ]
