# Generated by Django 2.1.5 on 2020-01-28 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_auto_20200126_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingtable',
            name='seenStatus',
            field=models.BooleanField(default=False),
        ),
    ]
