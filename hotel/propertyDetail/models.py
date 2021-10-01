from django.db import models
from datetime import datetime
from account.models import User
from django.core.validators import RegexValidator
import os
from faker.generator import random
from django.dispatch import receiver
from hotel.Country.models import Country
from account.models import User


def busn_reg_cert_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    user_id = instance.user.id
    instance_id = instance.id
    dir_name = 'document'
    renamed_file = 'busn_reg_cert' + str(instance.user.id)
    return 'user_{user_id}/{dir_name}/prop_{instance_id}/{renamed_file}{ext}'.format(user_id=user_id,
                                                                           basename=basefilename,
                                                                           dir_name=dir_name,
                                                                           instance_id=instance_id,
                                                                           renamed_file=renamed_file,
                                                                           ext=file_extension)
    #
    # return 'user_{instanceId}/prp/profile/{name}_{date}_{randomstring}{ext}'.format(instanceId=instance.user.id,
    #                                                                                   basename=basefilename,
    #                                                                                   randomstring=randomstr,
    #                                                                                   ext=file_extension,
    #                                                                                   name=instance.name.replace(" ",
    #                                                                                                              "_"),
    #                                                                                   date=instance.created_at.date())
    #

def busn_lcn_cert_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    user_id = instance.user.id
    instance_id = instance.id
    dir_name = 'document'
    renamed_file = 'busn_lcn_cert' + str(instance.user.id)
    return 'user_{user_id}/{dir_name}/prop_{instance_id}/{renamed_file}{ext}'.format(user_id=user_id,
                                                                           basename=basefilename,
                                                                           dir_name=dir_name,
                                                                           instance_id=instance_id,
                                                                           renamed_file=renamed_file,
                                                                           ext=file_extension)


def pan_card_cert_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    user_id = instance.user.id
    instance_id = instance.id
    dir_name = 'document'
    renamed_file = 'pan_card_cert' + str(instance.user.id)
    return 'user_{user_id}/{dir_name}/prop_{instance_id}/{renamed_file}{ext}'.format(user_id=user_id,
                                                                           basename=basefilename,
                                                                           dir_name=dir_name,
                                                                           instance_id=instance_id,
                                                                           renamed_file=renamed_file,
                                                                           ext=file_extension)


def vat_cert_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    user_id = instance.user.id
    instance_id = instance.id
    dir_name = 'document'
    renamed_file = 'vat_cert_path' + str(instance.user.id)
    return 'user_{user_id}/{dir_name}/prop_{instance_id}/{renamed_file}{ext}'.format(user_id=user_id,
                                                                           basename=basefilename,
                                                                           dir_name=dir_name,
                                                                           instance_id=instance_id,
                                                                           renamed_file=renamed_file,
                                                                           ext=file_extension)


class PropertyDetail(models.Model):
    legal_name = models.CharField(max_length=200, blank=True, null=True)
    business_name = models.CharField(max_length=200, blank=True, null=True)
    business_reg_date = models.CharField(max_length=60, null=True, blank=True)
    comm_open_date = models.CharField(max_length=60, null=True, blank=True)
    prop_history = models.CharField(max_length=200, blank=True, null=True)
    corp_address = models.CharField(max_length=200, blank=True, null=True)
    business_address = models.CharField(max_length=200, blank=True, null=True)
    comp_reg_name = models.CharField(max_length=200, blank=True, null=True)
    comp_reg_no = models.CharField(max_length=200, blank=True, null=True)
    bus_reg_no = models.CharField(max_length=200, blank=True, null=True)
    type_of_inc = models.CharField(max_length=200, blank=True, null=True)
    pan_number = models.CharField(max_length=60, null=True, blank=True)
    name_on_pancard = models.CharField(max_length=60, null=True, blank=True)
    vat_number = models.CharField(max_length=60, null=True, blank=True)
    busn_reg_cert = models.FileField(blank=True, default='default.png', upload_to=busn_reg_cert_path, max_length=100)
    busn_lcn_cert = models.FileField(blank=True, default='default.png', upload_to=busn_lcn_cert_path, max_length=100)
    pan_card_cert = models.FileField(blank=True, default='default.png', upload_to=pan_card_cert_path, max_length=100)
    vat_cert = models.FileField(blank=True, default='default.png', upload_to=vat_cert_path, max_length=100)
    car_rental = models.BooleanField(default=False)
    transport_company = models.BooleanField(default=False)
    travel_agency = models.BooleanField(default=False)
    food_deliver_agent = models.BooleanField(default=False)
    restaurant_bar_lounge = models.BooleanField(default=False)
    tour_operator = models.BooleanField(default=False)
    ticketing_agent = models.BooleanField(default=False)
    travel_agent = models.BooleanField(default=False)
    trekking_company = models.BooleanField(default=False)
    expedition_company = models.BooleanField(default=False)
    date = models.CharField(max_length=60, null=True, blank=True)
    applicant_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='created')

    def __str__(self):
        return self.legal_name

    # def delete(self, *args, **kwargs):
    #     self.image.delete()
    #     super().delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = "PropertyDetail"


class Accomodation(models.Model):
    acc_name = models.CharField(max_length=100, blank=True, null=True)
    prop_det = models.ForeignKey(PropertyDetail, on_delete=models.CASCADE)

# @receiver(models.signals.pre_save, sender=OwnerProfile)
# def auto_delete_file_on_change(sender, instance, **kwargs):
#     """
#     Deletes old file from filesystem
#     when corresponding `MediaFile` object is updated
#     with new file.
#     """
#     if not instance.pk:
#         return False
#
#     try:
#         old_file = sender.objects.get(pk=instance.pk).image
#     except sender.DoesNotExist:
#         return False
#
#     new_file = instance.image
#     if not old_file == new_file:
#         if os.path.isfile(old_file.path):
#             os.remove(old_file.path)
#
