from django import forms
from .models import Users
from .models import Address

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["contact","created_at", "image","dob","gender"]

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["city","state","country","address1", "address2", "contactno" ,'name' ,"is_primary", "user"]