# Generated by Django 2.1.5 on 2019-11-28 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0016_auto_20191127_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelinventory',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
