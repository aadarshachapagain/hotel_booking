# Generated by Django 2.1.5 on 2020-01-03 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditpoint',
            name='booking',
        ),
        migrations.RemoveField(
            model_name='rewardpoint',
            name='booking',
        ),
        migrations.RemoveField(
            model_name='virtualpoint',
            name='booking',
        ),
    ]