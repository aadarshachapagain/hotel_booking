# Generated by Django 2.1.5 on 2019-10-03 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_hotels_estd_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='cino',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='hotels',
            name='cname',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='hotels',
            name='nameonpancard',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='hotels',
            name='pannumber',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
