# Generated by Django 2.1.5 on 2020-03-06 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0048_merge_20200305_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childsupplementpolicy',
            name='inventory',
        ),
    ]
