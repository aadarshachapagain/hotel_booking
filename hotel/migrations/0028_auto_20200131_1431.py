# Generated by Django 2.1.5 on 2020-01-31 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0027_favourites_inventory_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotelgallery',
            options={'verbose_name_plural': 'Hotel Gallery'},
        ),
        migrations.AlterField(
            model_name='hotelgallery',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
