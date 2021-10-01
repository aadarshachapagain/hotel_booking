from django import forms
from ..models import Hotels
from ..amenities.models import HotelAmenities
from .models import HotelInventory


class HotelInvForm(forms.ModelForm):
    class Meta:
        model = HotelInventory
        fields = ["room_no",
                  "room_name",
                  "description",
                  "room_size",
                  "room_size_unit",
                  "hotel",
                  "user",
                  "no_of_rooms",
                  "created_at",
                  "infant_max",
                  "child_max",
                  "adult_max",
                  "extra_bed",
                  "no_of_extra_bed",
                  "image",
                  "priceforadult",
                  # "priceforchild",
                  "agerangeforinfant",
                  "discountforinfant",
                  "agerangeforchild",
                  "discountforchild",
                  "european_plan",
                  "bedandbreakfast_plan",
                  "roomtype",
                  "extra_crib",
                  "no_of_extra_crib",
                  "room_location"
                  ]
        
    def clean(self):
        super(HotelInvForm, self).clean()
        ep = self.cleaned_data.get('european_plan')
        bb = self.cleaned_data.get('bedandbreakfast_plan')

        if ep is None and bb is None:
            self.add_error('european_plan', 'Select at least one plan')
            self.add_error('bedandbreakfast_plan', 'Select at least one plan')

        elif ep is None:
            self.cleaned_data['european_plan'] = ''

        elif bb is None:
            self.cleaned_data['bedandbreakfast_plan'] = ''

        return self.cleaned_data
