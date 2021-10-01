# Generated by Django 2.1.5 on 2020-03-11 06:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0058_auto_20200311_0533'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimilarSystems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.BooleanField(blank=True, default=False)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
