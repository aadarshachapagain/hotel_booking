# Generated by Django 2.1.5 on 2020-04-03 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0085_auto_20200402_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertydetail',
            name='business_reg_date',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='propertydetail',
            name='comm_open_date',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='propertydetail',
            name='date',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
