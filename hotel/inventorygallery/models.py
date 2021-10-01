import os

from django.core.validators import RegexValidator
from django.db import models
import datetime
from django.dispatch import receiver


from faker.generator import random

from users.models import Users
from ..amenities.models import HotelAmenities
from ..inventory.models import HotelInventory


def photo_path(instance, filename):
    base_file_name, file_extension = os.path.splitext(filename)
    title = str(instance.title)
    replace_title_str = title.replace(' ', '_')
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_string = ''.join((random.choice(chars)) for x in range(5))
    return 'user_{userId}/images/hotel_{hotelId}/inventory_{inventoryId}/gallery_{title}_{random_string}_{date}{ext}'.format(
        userId=instance.hotel_inventory_id.hotel.owner_id.user.id,
        hotelId=instance.hotel_inventory_id.hotel.id,
        inventoryId=instance.hotel_inventory_id.id,
        base_name=base_file_name,
        random_string=random_string,
        title=replace_title_str,
        ext=file_extension,
        date=datetime.date.today()
    )


class InventoryGallery(models.Model):
    hotel_inventory_id = models.ForeignKey(
        HotelInventory, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(blank=True,default='default.png',upload_to= photo_path, max_length=500)
    title_regx = RegexValidator(regex=r'^[a-zA-Z]*$',
                                 message="You cannot enter number here.")
    title = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Hotel & Room Gallery"

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

# @receiver(models.signals.pre_save, sender=InventoryGallery)
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