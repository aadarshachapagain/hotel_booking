from django import forms

from .models import HotelInventory


class DefaultPriceForm(forms.ModelForm):
    class Meta:
        model = HotelInventory
        fields = [
                  "created_at",
                  "priceforadult",
                  "european_plan",
                  "bedandbreakfast_plan"
                  ]



    # def clean(self):
    #     super(HotelInvForm, self).clean()
    #     ep = self.cleaned_data.get('european_plan')
    #     bb = self.cleaned_data.get('bedandbreakfast_plan')
    #     print(ep)
    #     print(bb)
    #
    #     if ep is None and bb is None:
    #         self.add_error('european_plan', 'Select atleast one plan !')
    #         self.add_error('bedandbreakfast_plan', 'Select atleast one plan !')
    #
    #     elif ep is None:
    #         self.cleaned_data['european_plan'] = 0
    #
    #     elif bb is None:
    #         self.cleaned_data['bedandbreakfast_plan'] = 0
    #
    #     return self.cleaned_data
