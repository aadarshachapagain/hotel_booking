# Generated by Django 2.1.5 on 2020-03-19 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0073_auto_20200319_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryupdate',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
