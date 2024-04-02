from django.contrib import messages
from .models import QRGenerator
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect


# ESTA CLASE SIRVE PARA GUARDAR LA URL CUANDO EL TITULO ESTA PERSONALIZADO, OSEA NO ESTA VACIO
class TitleIsNotNone:
    def __init__(self, request, form) -> None:
        self.request = request
        self.form = form

    def save_when_title_is_not_none(self):
        try:
            create_new_url = QRGenerator()
            create_new_url.user = self.request.user.email
            create_new_url.original_url = self.form.cleaned_data['original_url']
            create_new_url.title = self.form.cleaned_data['title']
            create_new_url.short_url = self.form.cleaned_data['short_url']
            create_new_url.color_qr = self.form.cleaned_data['color_qr']
            create_new_url.bg_color_qr = self.form.cleaned_data['bg_color_qr']
            create_new_url.border_color_qr = self.form.cleaned_data['border_color_qr']
            create_new_url.border_qr = self.form.cleaned_data['border_qr']
            create_new_url.save()

            messages.success(self.request, 'The url short has been created')
            return redirect('dashboard')
        except:
            messages.error(
                self.request, 'Verify if you have copied correctly the url you want to shorten')
            return redirect('create_new_qr_codes')


# ESTA CLASE SIRVE PARA GUARDAR LA URL CUANDO EL TITULO NO ESTA VACIO Y ESTA PERSONALIZADO
class TitleIsNone:
    def __init__(self, request, form) -> None:
        self.request = request
        self.form = form

    def getting_title_window(self):
        url = self.form.cleaned_data['original_url']
        response = requests.get(url)
        try:
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                window_title = soup.title.string
                return window_title
        except:
            return None

    def save_when_title_is_none(self):
        # Si no introdujo nada, hacemos una peticion para obtener el titulo de la ventana del link a guardar
        try:
            create_new_url = QRGenerator()
            create_new_url.user = self.request.user.email
            create_new_url.original_url = self.form.cleaned_data['original_url']
            create_new_url.title = self.getting_title_window()
            create_new_url.short_url = self.form.cleaned_data['short_url']
            create_new_url.color_qr = self.form.cleaned_data['color_qr']
            create_new_url.bg_color_qr = self.form.cleaned_data['bg_color_qr']
            create_new_url.border_color_qr = self.form.cleaned_data['border_color_qr']
            create_new_url.border_qr = self.form.cleaned_data['border_qr']
            create_new_url.save()

            messages.success(
                self.request, 'The url short has been created')
            return redirect('dashboard')
        except:
            messages.error(
                self.request, 'Verify if you have copied correctly the url you want to shorten')
            return redirect('create_new_qr_codes')
