# Generated by Django 2.1.5 on 2020-04-22 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0115_auto_20200422_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelinventory',
            name='bedandbreakfast_plan',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='hotelinventory',
            name='european_plan',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
