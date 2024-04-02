from django import forms
from .models import QRGenerator


class CreateQRCodeForm(forms.ModelForm):
    class Meta:
        model = QRGenerator
        fields = ['title', 'original_url', 'short_url',
                  'color_qr', 'bg_color_qr', 'border_color_qr', 'border_qr']
