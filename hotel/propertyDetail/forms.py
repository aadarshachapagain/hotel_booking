from django import forms
from hotel.propertyDetail.models import PropertyDetail
from PIL import Image


class PropertyDetailForm(forms.ModelForm):
    class Meta:
        model = PropertyDetail
        fields = [
            "legal_name",
            "business_name",
            "business_reg_date",
            "comm_open_date",
            "prop_history",
            "corp_address",
            "business_address",
            "comp_reg_name",
            "comp_reg_no",
            "bus_reg_no",
            "type_of_inc",
            "pan_number",
            "name_on_pancard",
            "vat_number",
            "busn_reg_cert",
            "busn_lcn_cert",
            "pan_card_cert",
            "vat_cert",
            "car_rental",
            "transport_company",
            "travel_agency",
            "food_deliver_agent",
            "restaurant_bar_lounge",
            "tour_operator",
            "ticketing_agent",
            "travel_agent",
            "trekking_company",
            "expedition_company",
            "date",
            "applicant_name",
            "user"
        ]


class OwnerAndPropertyForm(forms.Form):
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # image = forms.ImageField()
    name = forms.CharField(max_length=200)

    # def save(self):
    #     print('self.data from save')
    #     photo = super(OwnerAndPropertyForm, self).save()
    #     x = self.cleaned_data.get('x')
    #     y = self.cleaned_data.get('y')
    #     w = self.cleaned_data.get('width')
    #     h = self.cleaned_data.get('height')
    #
    #     image = Image.open(photo.image)
    #     cropped_image = image.crop((x, y, w + x, h + y))
    #     # resized_image = cropped_image.resize((w, h), Image.ANTIALIAS)
    #     cropped_image.save(photo.image.path)
    #     return photo

# "name",
# "email",
# "contact",
# "image",
# "address",
# "is_owner",
# "is_manager",
# "Country",
# "document_type",
# "document",
# "created_at",
