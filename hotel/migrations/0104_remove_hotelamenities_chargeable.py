# Generated by Django 2.1.5 on 2020-04-14 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0103_hotelroomfeature_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelamenities',
            name='chargeable',
        ),
    ]