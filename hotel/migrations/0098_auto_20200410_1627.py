# Generated by Django 2.1.5 on 2020-04-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0097_auto_20200410_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory_bed_type',
            name='bed_count',
        ),
        migrations.AddField(
            model_name='bedtype',
            name='count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
