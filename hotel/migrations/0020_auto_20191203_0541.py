# Generated by Django 2.1.5 on 2019-12-03 05:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0019_merge_20191202_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoteladdress',
            name='contact1',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+977-9849755595'. Up to 15 digits allowed.", regex='^\\+?1?\\d{3}\\-?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='hoteladdress',
            name='contact2',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+977-9849755595'. Up to 15 digits allowed.", regex='^\\+?1?\\d{3}\\-?1?\\d{9,15}$')]),
        ),
    ]
