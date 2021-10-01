# Generated by Django 2.1.5 on 2020-02-06 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0029_bankdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='landmark',
            name='latitude',
            field=models.DecimalField(decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='landmark',
            name='longitude',
            field=models.DecimalField(decimal_places=16, max_digits=22, null=True),
        ),
    ]