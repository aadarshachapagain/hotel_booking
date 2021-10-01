# Generated by Django 2.1.5 on 2020-03-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0075_auto_20200319_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='cribspolicy',
            name='day',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='cribspolicy',
            name='season_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cribspolicy',
            name='season_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
