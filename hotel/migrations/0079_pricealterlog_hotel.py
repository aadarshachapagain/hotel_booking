# Generated by Django 2.1.5 on 2020-03-22 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0078_pricealterlog_altered_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricealterlog',
            name='hotel',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
