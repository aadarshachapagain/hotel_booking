from PIL import Image
from django import forms

from .models import HotelGallery


class HotelGalleryForm(forms.ModelForm):
    class Meta:
        model = HotelGallery
        fields = ['image', 'title', 'hotel_id']

    
