# Generated by Django 2.1.5 on 2019-10-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='estd_date',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
