# Generated by Django 2.1.5 on 2020-04-07 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0091_auto_20200407_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertydetail',
            name='status',
            field=models.CharField(default='created', max_length=20),
        ),
    ]
