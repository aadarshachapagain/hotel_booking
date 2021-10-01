import os

from django.db import models
from datetime import datetime

from django.dispatch import receiver
from faker.generator import random

from account.models import User
from django.core.validators import RegexValidator
import os
from faker.generator import random
from django.dispatch import receiver
from hotel.Country.models import Country


def doc_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    return '{dir_name}/doc_{randomstring}{ext}'.format(dir_name='owner_doc' + str(instance.user.id),
                                                       basename=basefilename,
                                                       randomstring=randomstr,
                                                       ext=file_extension)


def photo_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(5))
    return 'user_{instanceId}/image/profile/{name}_{date}_{randomstring}{ext}'.format(instanceId=instance.user.id,basename=basefilename,
                                                                             randomstring=randomstr,
                                                                             ext=file_extension,
                                                                              name=instance.name.replace(" ", "_"),
                                                                              date = instance.created_at.date())

class OwnerProfile(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                               null=True)  # validators should be a list
    email = models.EmailField(unique=True, null=True, blank=True)
    image = models.ImageField(blank=True, default='default.png', upload_to=photo_path, max_length=500)
    address = models.CharField(max_length=80, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_owner = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    Country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    document_type = models.CharField(max_length=30, blank=True, null=True)
    document = models.FileField(blank=True, default='default.png', upload_to=doc_path, max_length=100)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Owners Profile"


@receiver(models.signals.pre_save, sender=OwnerProfile)
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



