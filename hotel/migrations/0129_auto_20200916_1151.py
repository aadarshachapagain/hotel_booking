# Generated by Django 2.1.5 on 2020-09-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0128_inventoryupdate_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryupdate',
            name='is_available',
            field=models.CharField(default='', max_length=80, null=True),
        ),
    ]