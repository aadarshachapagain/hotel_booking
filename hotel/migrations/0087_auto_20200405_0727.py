# Generated by Django 2.1.5 on 2020-04-05 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0086_auto_20200403_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertydetail',
            name='applicant_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]