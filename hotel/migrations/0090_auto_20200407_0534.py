# Generated by Django 2.1.5 on 2020-04-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0089_propertydetail_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertydetail',
            name='is_verified',
        ),
        migrations.AddField(
            model_name='propertydetail',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]