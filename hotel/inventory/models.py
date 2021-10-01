import os
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver

from datetime import datetime
from faker.generator import random
from django.db.models.signals import post_save

from account.models import User
from hotel.models import Hotels
from hotel.amenities.models import HotelAmenities
from hotel.room_facilities.models import RoomFacilities
from hotel.roomfeature.models import HotelRoomFeature
from hotel.roomtype.models import HotelRoomType
from django.conf import settings
import shutil

def photo_path(instance, filename):
    """
    This method provides appropriate path to image.
    :param instance: current hotel inventory
    :param filename: name of file
    :return: path where is allocated to be saved
    """
    base_file_name, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_string = ''.join((random.choice(chars)) for x in range(5))
    return 'user_{userId}/images/hotel_{hotelId}/inventory_{inventoryId}/thumbnail_{date}{ext}'.format(
        userId=instance.user.id,
        hotelId=instance.hotel.id,
        inventoryId=instance.id,
        base_name=base_file_name,
        random_string=random_string,
        ext=file_extension,
        date=instance.created_at.date())


class HotelInventory(models.Model):
    """
    This class is used to save all the information related to room.
    """
    # field listed in the document
    room_no = models.IntegerField(blank=True, null=True)
    room_name = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    room_size = models.CharField(max_length=100, blank=True, null=True)
    room_size_unit = models.CharField(max_length=30, blank=True, null=True)
    room_location = models.CharField(max_length=100, blank=True, null=True)
    adult_max = models.IntegerField(validators=[MinValueValidator(1),
                                                MaxValueValidator(100)])
    infant_max = models.IntegerField(validators=[MinValueValidator(0),
                                                 MaxValueValidator(10)], null=True, blank=True)
    child_max = models.IntegerField(validators=[MinValueValidator(0),
                                                MaxValueValidator(10)])
    european_plan = models.DecimalField(max_digits=10, decimal_places=2,  blank=True, null=True)
    bedandbreakfast_plan = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    extra_bed = models.BooleanField(default=False, blank=True)
    no_of_extra_bed = models.IntegerField(blank=True, null=True)
    extra_crib = models.BooleanField(default=False, blank=True)
    no_of_extra_crib = models.IntegerField(blank=True, null=True)
    image = models.ImageField(default='default.png', upload_to=photo_path, max_length=500)
    status = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    # extra fields which are not listed in document, but can be needed in future.
    no_of_rooms = models.IntegerField(blank=True)
    priceforadult = models.TextField(blank=True)
    agerangeforinfant = models.CharField(max_length=30, blank=True, null=True)
    discountforinfant = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    agerangeforchild = models.CharField(max_length=30, blank=True, null=True)
    discountforchild = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # foreign key
    hotel = models.ForeignKey(Hotels, related_name="inventory", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amenities = models.ManyToManyField(HotelAmenities, through='hotelinventory_amenities')
    roomfeatures = models.ManyToManyField(HotelRoomFeature, through='hotelinventory_roomfeatures')
    roomtype = models.ForeignKey(HotelRoomType, related_name="roomtype", on_delete=models.CASCADE, null=True)
    roomfacility = models.ManyToManyField(RoomFacilities, through='hotelinventory_roomfacility')
    
    class Meta:
        verbose_name_plural = "Hotel Inventory"


# @receiver(post_save, sender=HotelInventory)
def update_image_path(sender, instance, created, **kwargs):
    if created:
        imagefile = instance.image
        old_name = imagefile.name
        if not old_name:
            return
        new_name = os.path.basename(old_name)
        new_path = os.path.join(settings.MEDIA_ROOT, photo_path(instance, new_name))
        if not os.path.exists(new_path):
            os.makedirs(os.path.dirname(new_path))
        os.rename(imagefile.path, new_path)
        instance.image.name = photo_path(instance, new_name)
        instance.save()

# @receiver(models.signals.pre_save, sender=HotelInventory)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class hotelinventory_roomfacility(models.Model):
    hotelinventory = models.ForeignKey(HotelInventory, related_name="inventory_for_facility", on_delete=models.CASCADE, null=True,
                                       blank=True)
    roomfacility = models.ForeignKey(RoomFacilities, related_name="roomfacility",
                                         on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    cost = models.CharField(max_length=20, null=True, blank=True)

class hotelinventory_roomfeatures(models.Model):
    hotelinventory = models.ForeignKey(HotelInventory, related_name="inventory", on_delete=models.CASCADE, null=True,
                                       blank=True)
    hotelroomfeature = models.ForeignKey(HotelRoomFeature, related_name="roomfeature",
                                         on_delete=models.CASCADE, null=True, blank=True)

#
# class hotelinventory_roomtype(models.Model):
#     hotelinventory = models.ForeignKey(HotelInventory, related_name="hotelinventory", on_delete=models.CASCADE)
#     hotelroomtype = models.ForeignKey(HotelRoomType, related_name="roomtype",
#                                       on_delete=models.CASCADE)


class hotelinventory_amenities(models.Model):
    hotelinventory = models.ForeignKey(HotelInventory, related_name="inventory_hotel", on_delete=models.CASCADE,
                                       null=True, blank=True)
    hotelamenities = models.ForeignKey(HotelAmenities, related_name="amenities",
                                       on_delete=models.CASCADE, null=True, blank=True)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
