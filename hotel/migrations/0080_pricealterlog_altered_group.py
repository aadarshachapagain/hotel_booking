# Generated by Django 2.1.5 on 2020-03-22 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0079_pricealterlog_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricealterlog',
            name='altered_group',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]