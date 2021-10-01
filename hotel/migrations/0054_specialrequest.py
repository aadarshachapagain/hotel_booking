# Generated by Django 2.1.5 on 2020-03-08 05:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0053_auto_20200308_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='specialRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.BooleanField(default=False)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialRequest', to='hotel.Hotels')),
            ],
            options={
                'verbose_name_plural': 'Special Request',
            },
        ),
    ]
