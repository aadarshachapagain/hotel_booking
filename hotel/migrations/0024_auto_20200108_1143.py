# Generated by Django 2.1.5 on 2020-01-08 05:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0023_inventoryupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoteladdress',
            name='contact1',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+977-9849755595'. Up to 15 digits allowed.", regex='^\\+?1?\\d{3}\\-?1?\\d{7,15}$')]),
        ),
        migrations.AlterField(
            model_name='hoteladdress',
            name='contact2',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+977-9849755595'. Up to 15 digits allowed.", regex='^\\+?1?\\d{3}\\-?1?\\d{7,15}$')]),
        ),
    ]