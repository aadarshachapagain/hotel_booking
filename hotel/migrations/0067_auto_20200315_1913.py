# Generated by Django 2.1.5 on 2020-03-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0066_auto_20200315_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryupdate',
            name='bedandbreakfast_plan',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryupdate',
            name='european_plan',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
