# Generated by Django 2.1.5 on 2020-01-12 08:03

from django.db import migrations, models
import hotel.gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0024_auto_20200108_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelgallery',
            name='image',
            field=models.ImageField(blank=True, default='default.png', max_length=500, upload_to=hotel.gallery.models.photo_path),
        ),
    ]
