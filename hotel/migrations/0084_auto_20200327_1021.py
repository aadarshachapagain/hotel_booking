# Generated by Django 2.1.5 on 2020-03-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0083_grouprate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grouprate',
            old_name='cost',
            new_name='ap_cost',
        ),
        migrations.AddField(
            model_name='grouprate',
            name='map_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
