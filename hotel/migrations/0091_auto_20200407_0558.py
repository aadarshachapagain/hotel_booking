# Generated by Django 2.1.5 on 2020-04-07 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0090_auto_20200407_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertydetail',
            name='status',
            field=models.CharField(default='pending_approval', max_length=20),
        ),
    ]
