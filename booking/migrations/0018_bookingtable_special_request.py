# Generated by Django 2.1.5 on 2020-02-07 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0017_bookingtable_seenstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingtable',
            name='special_request',
            field=models.TextField(blank=True, null=True),
        ),
    ]
