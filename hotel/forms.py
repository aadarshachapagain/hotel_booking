from django import forms
from .models import Hotels


# from tinymce import TinyMCE

# class TinyMCEWidget(TinyMCE):
#     def use_required_attribute(self, *args):
#         return False


class HotelForm(forms.ModelForm):
    # description = forms.CharField(
    #     widget=TinyMCEWidget(
    #         attrs={'required': False, 'cols': 30, 'rows': 10}
    #         )
    #         )
    class Meta:
        model = Hotels
        fields = [
            # "name",
            # "estd_date",
            # "cname",
            # "cino",
            # "pannumber",
            # "nameonpancard",
            "owner_id",
            "created_at",
            "description",
            "wordsbyowner",
            "image",
            "number_of_staff",
            "number_of_room",
            "star_rating",
            "check_in",
            "check_out",
            "ratefornepali",
            "rateforsaarc",
            "rateforforeign",
            "prop_id"
        ]
