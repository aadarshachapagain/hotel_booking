from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from account.models import User
from hotel.owner.models import HotelOwner
from hotel.staff.models import HotelStaff


class OwnerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    # first_name = forms.CharField(required=True, label='First Name')
    # last_name = forms.CharField(required=True, label='Last Name')

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ("email", "username", "password1", "password2", "account_type")
        fields = ("email", "password1", "password2", "account_type")


#
# class UserAccountUpdateForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model=User
#         fields=("account_type")

# @transaction.atomic
# def save(self):
#     user=super().save(commit=False)
#     user.is_hotel_owner=True
#     user.is_active = False
#     user.save()
#     owner=HotelOwner.objects.create(user=user)
#     return user

class StaffSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields=("first_name","last_name","email","username","password1","password2","account_type")
        fields = ("email", "username", "password1", "password2", "account_type")
        fields = ("email", "password1", "password2", "account_type")


class NormalUSerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(required=True, label='First Name')
    last_name = forms.CharField(required=True, label='Last Name')

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ("email", "username", "password1", "password2", "account_type")
        fields = ("email", "password1", "password2", "account_type")

    # @transaction.atomic
    # def save(self):
    #     user=super().save(commit=False)
    #     user.is_hotel_staff=True
    #     user.save()
    #     travel_tour_staff=HotelStaff.objects.create(user=user)
    #     return user
