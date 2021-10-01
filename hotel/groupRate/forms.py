from django import forms
from hotel.child_supplement_policy.models import ChildSupplementPolicy
from hotel.inventory.models import HotelInventory
from hotel.models import Hotels
from hotel.groupRate.models import GroupRate



class GroupRateForm(forms.ModelForm):
    hotel = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=Hotels.objects.all(), empty_label=None)
    range_start = forms.IntegerField()
    range_end = forms.IntegerField()
    map_cost = forms.DecimalField(label='MAP Price', widget=forms.TextInput(attrs={'style': 'height:28px'}),
                                  required=False, help_text='This price is on per person basis')
    ap_cost = forms.DecimalField(label=' AP Price', widget=forms.TextInput(attrs={'style': 'height:28px'}),
                                 required=False, help_text='This price is on per person basis')



    class Meta:
        model = GroupRate
        fields = [
            "range_start",
            "range_end",
            "map_cost",
            "ap_cost",
            "hotel",
        ]

    # class Media:
    #     js = ('js/hotelInventoryChildSupplement.js',)
