# Generated by Django 2.1.5 on 2020-03-19 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0074_inventoryupdate_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancellation_policy',
            name='day',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
