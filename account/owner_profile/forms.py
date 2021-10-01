from PIL import Image
from django import forms
from .models import OwnerProfile


class OwnerProfileForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = OwnerProfile

        fields = ["name",
                  "email",
                  "contact",
                  "image",
                  "address",
                  "is_owner",
                  "is_manager",
                  "Country",
                  "document_type",
                  "document",
                  "created_at",
                  "x",
                  "y",
                  "width",
                  "height"
                  ]


    def save(self):
        photo = super(OwnerProfileForm, self).save()
        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        
        if x!= None:
            image = Image.open(photo.image)
            cropped_image = image.crop((x, y, w+x, h+y))
            cropped_image.save(photo.image.path)
        return photo


