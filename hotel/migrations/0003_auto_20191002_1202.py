# Generated by Django 2.1.5 on 2019-10-02 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20191002_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cancellation_policy',
            old_name='inventory',
            new_name='hotel',
        ),
        migrations.RenameField(
            model_name='cancellation_policy',
            old_name='day',
            new_name='hour',
        ),
    ]
