# Generated by Django 4.0.1 on 2022-01-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fahadsapp', '0006_uploadportfolio_image_height_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadportfolio',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='uploadportfolio',
            name='image_width',
        ),
        migrations.AlterField(
            model_name='uploadportfolio',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='thumbnail'),
            preserve_default=False,
        ),
    ]
