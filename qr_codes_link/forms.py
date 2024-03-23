from django import forms
from .models import QRGenerator


class CreateQRCodeForm(forms.ModelForm):
    class Meta:
        model = QRGenerator
        fields = ['user', 'title', 'original_url', 'url_short', 'qr_image']
