# Generated by Django 2.1.5 on 2020-04-19 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0112_auto_20200418_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelinventory',
            name='room_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]