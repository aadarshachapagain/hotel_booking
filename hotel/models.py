import os

from django.db import models
from datetime import datetime

from django.dispatch import receiver
from faker.generator import random

from hotel.CreditCard.models import CreditCard
from hotel.hotel_facilities.models import HotelFacilities
from travel.utils import all_percentage_complete
from .owner.models import HotelOwner
from account.owner_profile.models import OwnerProfile
from account.Language.models import Language
from django.db import connection
from hotel.propertyDetail.models import PropertyDetail
from django.conf import settings



# from tinymce.models import HTMLField

def photo_path(instance, filename):
    base_file_name, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_string = ''.join((random.choice(chars)) for x in range(5))
    return 'user_{userId}/images/hotel_{hotelId}/thumbnail_{date}{ext}'.format(
        userId=instance.owner_id.user.id,
        hotelId=instance.id,
        base_name=base_file_name,
        random_string=random_string,
        ext=file_extension,
        date=instance.created_at.date())


class Hotels(models.Model):
    # name = models.CharField(max_length=200)
    # estd_date = models.CharField(max_length=60, null=True, blank=True)
    # cname = models.CharField(max_length=60, null=True, blank=True)
    # cino = models.CharField(max_length=60, null=True, blank=True)
    # pannumber = models.CharField(max_length=60, null=True, blank=True)
    # nameonpancard = models.CharField(max_length=60, null=True, blank=True)
    owner_id = models.ForeignKey(OwnerProfile, on_delete=models.CASCADE)
    number_of_room = models.IntegerField(default=0)
    number_of_staff = models.IntegerField(default=0)
    wordsbyowner = models.TextField(blank=True, default='words by owner')
    description = models.TextField(blank=True, null=True)
    star_rating = models.CharField(max_length=40, blank=True)
    check_in = models.TimeField(blank=True, null=True)
    check_out = models.TimeField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(default='default.png', upload_to=photo_path, max_length=500)

    # rate for different citizens
    rateforforeign = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ratefornepali = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rateforsaarc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # rate for different citizens

    created_at = models.DateTimeField(default=datetime.now, blank=True)
    facilities = models.ManyToManyField(HotelFacilities, through="HotelFacilitiesMiddle", related_name='facilitiess')
    languages = models.ManyToManyField(Language, through="HotelLanguageMiddle", related_name='languages')
    prop_id = models.ForeignKey(PropertyDetail, on_delete=models.CASCADE, null=True, blank=True)

    # def __str__(self):
    #     return self.prop_id

    class Meta:
        verbose_name_plural = "Hotels"

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    @property
    def percentage_complete(self):
        return all_percentage_complete(self)

@receiver(models.signals.post_save, sender=Hotels)
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

@receiver(models.signals.pre_save, sender=Hotels)
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


class HotelFacilitiesMiddle(models.Model):
    hotels = models.ForeignKey(Hotels, related_name="hotel", on_delete=models.CASCADE)
    hotelsfacilities = models.ForeignKey(HotelFacilities, related_name="hotelfacility", on_delete=models.CASCADE)
    freeorpaid = models.CharField(default='Free', max_length=10)
    description = models.CharField(max_length=400, blank=True, null=True)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    isrecomended = models.CharField(default='No', max_length=10, )

    class Meta:
        verbose_name_plural = "HotelFacilitiesMiddle"

    def __str__(self):
        return self.hotels.id

    def max_use(self):
        with connection.cursor() as cursor:
            cursor.execute(
                'SELECT hotelsfacilities_id,COUNT(hotelsfacilities_id) AS value_occurrence FROM hotel_hotelfacilitiesmiddle GROUP BY hotelsfacilities_id ORDER BY value_occurrence DESC LIMIT 10;')
            row = cursor.fetchall()
        return row


class HotelLanguageMiddle(models.Model):
    hotels = models.ForeignKey(Hotels, related_name="hotel_language", on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name="hotelfacility", on_delete=models.CASCADE)


class HotelsNew(models.Model):
    oldhotelid = models.IntegerField()
    name = models.CharField(max_length=200)
    owner_id = models.ForeignKey(OwnerProfile, on_delete=models.CASCADE)
    number_of_room = models.IntegerField(default=0)
    number_of_staff = models.IntegerField(default=0)
    wordsbyowner = models.TextField(blank=True, default='words by owner')
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(default='default.png')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    facilities = models.ManyToManyField(HotelFacilities, through="HotelFacilitiesMiddleNew",
                                        related_name='facilitiessNew')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "HotelsNew"

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)


class HotelFacilitiesMiddleNew(models.Model):
    hotels = models.ForeignKey(HotelsNew, related_name="hotelnew", on_delete=models.CASCADE)
    hotelsfacilities = models.ForeignKey(HotelFacilities, related_name="hotelfacilitynew", on_delete=models.CASCADE)
