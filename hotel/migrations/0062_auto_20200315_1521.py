# Generated by Django 2.1.5 on 2020-03-15 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0061_cancellation_policy_change_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='childsupplementpolicy',
            name='hotelInventory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.HotelInventory'),
        ),
        migrations.AddField(
            model_name='childsupplementpolicy',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.ChildSupplementPolicy'),
        ),
    ]
