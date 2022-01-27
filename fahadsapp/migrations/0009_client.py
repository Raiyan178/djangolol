# Generated by Django 4.0.1 on 2022-01-25 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fahadsapp', '0008_uploadportfolio_threed'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('commentcl', models.CharField(max_length=200)),
                ('imgcl', models.ImageField(default='img/testimonials/t1.jpg', upload_to='clientimg')),
                ('ratecl', models.DecimalField(decimal_places=3, max_digits=3)),
            ],
        ),
    ]
