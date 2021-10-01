# Generated by Django 2.1.5 on 2019-11-27 09:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0013_auto_20191127_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorygallery',
            name='title',
            field=models.CharField(blank=True, max_length=200, validators=[django.core.validators.RegexValidator(message='You cannot enter number here.', regex='/^[0-9]+$/')]),
        ),
    ]