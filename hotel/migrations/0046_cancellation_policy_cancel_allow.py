# Generated by Django 2.1.5 on 2020-03-02 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0045_auto_20200302_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancellation_policy',
            name='cancel_allow',
            field=models.BooleanField(default=False),
        ),
    ]
