import os

from django.db import models
from datetime import datetime

from django.db.models import Count
from faker.generator import random
from django.dispatch import receiver

from travel.utils import hotel_gallery_percentage_complete
from users.models import Users
from ..amenities.models import HotelAmenities
from ..models import Hotels
from ..inventory.models import HotelInventory


def photo_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(5))
    return 'user_{userId}/images/hotel_{instanceId}/{title}/{name}_{randomstring}_{date}{ext}'.format(
        userId=instance.hotel_id.owner_id.user.id,
        instanceId=instance.hotel_id.id,
        basename=basefilename,
        randomstring=randomstr,
        ext=file_extension,
        title=instance.title,
        name=instance.title.replace(" ", "_"),
        date=instance.created_at.date())

class HotelGallery(models.Model):
    hotel_id = models.ForeignKey(Hotels,related_name='galleries', on_delete=models.CASCADE, blank=True)
    image = models.ImageField(blank=True,default='default.png',upload_to= photo_path, max_length=500)
    title = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Hotel Gallery"

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    
    def templates(self):
        templates = ['Building', 'Lobby', 'Kitchen', 'Restaurant']
        return templates
    
    @property
    def percentage_complete(self):
        templates = HotelGallery.templates(self)
        temp = HotelGallery.objects.filter(hotel_id=self.hotel_id.id, title__in=templates)
        a = temp.values('title').annotate(dcount=Count('title'))
        # since there are four templates for building, restaurant, lobby, kitchen
        required_count = 4
        return hotel_gallery_percentage_complete(a.count(), required_count)

    @property
    def allow(self):
        temp = HotelGallery.objects.filter(hotel_id=self.hotel_id.id).count()
        # since there are four templates for building, restaurant, lobby, kitchen
        required_count = 4
        if temp == required_count:
            return 'no'
        else:
            return 'go'
    
@receiver(models.signals.pre_save, sender=HotelGallery)
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