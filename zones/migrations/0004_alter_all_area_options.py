# Generated by Django 4.0.4 on 2022-05-15 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zones', '0003_remove_area_image_all_area'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='all_area',
            options={'verbose_name': 'Ваши полигон', 'verbose_name_plural': 'Ваши полигоны'},
        ),
    ]
