# Generated by Django 2.1.5 on 2020-02-10 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0032_auto_20200207_0535'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddOnServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('flatorpercent', models.BooleanField(blank=True, default=False)),
                ('is_recommended', models.CharField(blank=True, max_length=80, null=True)),
                ('amenities', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.HotelAmenities')),
                ('inventory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.HotelInventory')),
            ],
            options={
                'verbose_name_plural': 'AddOnServices',
            },
        ),
    ]
