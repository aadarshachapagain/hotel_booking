# Generated by Django 2.1.5 on 2019-10-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_merge_20191003_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
