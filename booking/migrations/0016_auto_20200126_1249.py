# Generated by Django 2.1.5 on 2020-01-26 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0015_auto_20200120_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingtable',
            name='status',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
