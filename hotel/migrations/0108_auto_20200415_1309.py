# Generated by Django 2.1.5 on 2020-04-15 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0107_auto_20200415_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelinventory_roomtype',
            name='hotelinventory',
        ),
        migrations.RemoveField(
            model_name='hotelinventory_roomtype',
            name='hotelroomtype',
        ),
        migrations.RemoveField(
            model_name='hotelinventory',
            name='roomtype',
        ),
        migrations.AddField(
            model_name='hotelinventory',
            name='roomtype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roomtype', to='hotel.HotelRoomType'),
        ),
        migrations.DeleteModel(
            name='hotelinventory_roomtype',
        ),
    ]
