# Generated by Django 2.1.5 on 2020-03-02 08:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0042_b2b_group_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b2b',
            name='group_size',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
