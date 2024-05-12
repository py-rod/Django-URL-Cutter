from django import forms
from .models import ModelQR


class CreateQRCodeForm(forms.ModelForm):
    class Meta:
        model = ModelQR
        fields = ['title', 'original_url', 'short_url',
                  'color_qr', 'bg_color_qr', 'border_color_qr', 'border_qr']
