# Generated by Django 2.1.5 on 2020-03-01 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0042_hotelamenities_chargeable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelinventory',
            name='price',
        ),
    ]