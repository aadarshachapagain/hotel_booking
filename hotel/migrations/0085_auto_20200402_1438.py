# Generated by Django 2.1.5 on 2020-04-02 14:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hotel.propertyDetail.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0084_auto_20200327_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_name', models.CharField(blank=True, max_length=200, null=True)),
                ('business_name', models.CharField(blank=True, max_length=200, null=True)),
                ('business_reg_date', models.DateField(blank=True, null=True)),
                ('comm_open_date', models.DateField(blank=True, null=True)),
                ('prop_history', models.CharField(blank=True, max_length=200, null=True)),
                ('corp_address', models.CharField(blank=True, max_length=200, null=True)),
                ('business_address', models.CharField(blank=True, max_length=200, null=True)),
                ('comp_reg_name', models.CharField(blank=True, max_length=200, null=True)),
                ('comp_reg_no', models.CharField(blank=True, max_length=200, null=True)),
                ('bus_reg_no', models.CharField(blank=True, max_length=200, null=True)),
                ('type_of_inc', models.CharField(blank=True, max_length=200, null=True)),
                ('pan_number', models.CharField(blank=True, max_length=60, null=True)),
                ('name_on_pancard', models.CharField(blank=True, max_length=60, null=True)),
                ('vat_number', models.CharField(blank=True, max_length=60, null=True)),
                ('busn_reg_cert', models.FileField(blank=True, default='default.png', upload_to=hotel.propertyDetail.models.busn_reg_cert_path)),
                ('busn_lcn_cert', models.FileField(blank=True, default='default.png', upload_to=hotel.propertyDetail.models.busn_lcn_cert_path)),
                ('pan_card_cert', models.FileField(blank=True, default='default.png', upload_to=hotel.propertyDetail.models.pan_card_cert_path)),
                ('vat_cert', models.FileField(blank=True, default='default.png', upload_to=hotel.propertyDetail.models.vat_cert_path)),
                ('car_rental', models.BooleanField(default=False)),
                ('transport_company', models.BooleanField(default=False)),
                ('travel_agency', models.BooleanField(default=False)),
                ('food_deliver_agent', models.BooleanField(default=False)),
                ('restaurant_bar_lounge', models.BooleanField(default=False)),
                ('tour_operator', models.BooleanField(default=False)),
                ('ticketing_agent', models.BooleanField(default=False)),
                ('travel_agent', models.BooleanField(default=False)),
                ('trekking_company', models.BooleanField(default=False)),
                ('expedition_company', models.BooleanField(default=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('applicant_name', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'PropertyDetail',
            },
        ),
        migrations.AddField(
            model_name='accomodation',
            name='prop_det',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.PropertyDetail'),
        ),
    ]