from django.contrib import messages
from .models import ModelQR
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from url_link.models import ModelUrl
import random
import string


def check_short_url_qr(short_url):
    return ModelQR.objects.filter(short_url=short_url).exists()


def check_short_url_link(short_url):
    return ModelUrl.objects.filter(short_url=short_url).exists()


def generate_short_url():
    random_digits_for_ur = ''.join(random.choices(
        f'{string.ascii_lowercase}{string.ascii_uppercase}{string.digits}', k=9))

    return f'{random_digits_for_ur}'


# ESTA CLASE SIRVE PARA GUARDAR LA URL CUANDO EL TITULO ESTA PERSONALIZADO, OSEA NO ESTA VACIO
class TitleIsNotNone:
    def __init__(self, request, form) -> None:
        self.request = request
        self.form = form

    def save_when_title_is_not_none(self):
        try:
            # SHORT URL DEL FORM
            short_url_form = self.form.cleaned_data['short_url']

            # CONDICION SI EL SHORT URL VIENE VACIO
            if bool(short_url_form) == False:
                # SHORT URL GENERADO DE MANERA ALEATORIA
                new_short_url = generate_short_url()

                if check_short_url_link(new_short_url) == False and check_short_url_qr(new_short_url) == False:

                    create_new_qr = ModelQR()
                    create_new_qr.user = self.request.user.email
                    create_new_qr.original_url = self.form.cleaned_data['original_url']
                    create_new_qr.title = self.form.cleaned_data['title']
                    create_new_qr.short_url = new_short_url
                    create_new_qr.color_qr = self.form.cleaned_data['color_qr']
                    create_new_qr.bg_color_qr = self.form.cleaned_data['bg_color_qr']
                    create_new_qr.border_color_qr = self.form.cleaned_data['border_color_qr']
                    create_new_qr.border_qr = self.form.cleaned_data['border_qr']
                    create_new_qr.type_app = 'qr'
                    create_new_qr.save()

                    messages.success(
                        self.request, 'The QR Code has been created')
                    return redirect('dashboard')

                elif check_short_url_link(new_short_url) or check_short_url_qr(new_short_url):

                    create_new_qr = ModelQR()
                    create_new_qr.user = self.request.user.email
                    create_new_qr.original_url = self.form.cleaned_data['original_url']
                    create_new_qr.title = self.form.cleaned_data['title']

                    while check_short_url_link(new_short_url) or check_short_url_qr(new_short_url):
                        create_new_qr.short_url = generate_short_url()

                    create_new_qr.color_qr = self.form.cleaned_data['color_qr']
                    create_new_qr.bg_color_qr = self.form.cleaned_data['bg_color_qr']
                    create_new_qr.border_color_qr = self.form.cleaned_data['border_color_qr']
                    create_new_qr.border_qr = self.form.cleaned_data['border_qr']
                    create_new_qr.type_app = 'qr'
                    create_new_qr.save()

                    messages.success(
                        self.request, 'The QR Code has been created')
                    return redirect('dashboard')

            if bool(short_url_form):
                if check_short_url_link(short_url_form) == False and check_short_url_qr(short_url_form) == False:
                    create_new_qr = ModelQR()
                    create_new_qr.user = self.request.user.email
                    create_new_qr.original_url = self.form.cleaned_data['original_url']
                    create_new_qr.title = self.form.cleaned_data['title']
                    create_new_qr.short_url = short_url_form
                    create_new_qr.color_qr = self.form.cleaned_data['color_qr']
                    create_new_qr.bg_color_qr = self.form.cleaned_data['bg_color_qr']
                    create_new_qr.border_color_qr = self.form.cleaned_data['border_color_qr']
                    create_new_qr.border_qr = self.form.cleaned_data['border_qr']
                    create_new_qr.type_app = 'qr'
                    create_new_qr.save()

                    messages.success(
                        self.request, 'The QR Code has been created')
                    return redirect('dashboard')

            if bool(short_url_form):
                if check_short_url_link(short_url_form) or check_short_url_qr(short_url_form):
                    messages.error(
                        self.requests, 'This custom back-half is already exists. Try another one')
                    return redirect('create_new_qr_codes')

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
        try:
            # SHORT URL DEL FORM
            short_url_form = self.form.cleaned_data['short_url']

            # CONDICION SI EL SHORT URL VIENE VACIO
            if bool(short_url_form) == False:
                # SHORT URL GENERADO DE MANERA ALEATORIA
                new_short_url = generate_short_url()

                if check_short_url_link(new_short_url) == False and check_short_url_qr(new_short_url) == False:

                    create_new_qr = ModelQR()
                    create_new_qr.user = self.request.user.email
                    create_new_qr.original_url = self.form.cleaned_data['original_url']
                    create_new_qr.title = self.getting_title_window()
                    create_new_qr.short_url = new_short_url
                    create_new_qr.color_qr = self.form.cleaned_data['color_qr']
                    create_new_qr.bg_color_qr = self.form.cleaned_data['bg_color_qr']
                    create_new_qr.border_color_qr = self.form.cleaned_data['border_color_qr']
                    create_new_qr.border_qr = self.form.cleaned_data['border_qr']
                    create_new_qr.type_app = 'qr'
                    create_new_qr.save()

                    messages.success(
                        self.request, 'The QR Code has been created')
                    return redirect('dashboard')

                elif check_short_url_link(new_short_url) or check_short_url_qr(new_short_url):

                    create_new_qr = ModelQR()
                    create_new_qr.user = self.request.user.email
                    create_new_qr.original_url = self.form.cleaned_data['original_url']
                    create_new_qr.title = self.getting_title_window()

                    while check_short_url_link(new_short_url) or check_short_url_qr(new_short_url):
                        create_new_qr.short_url = generate_short_url()

                    create_new_qr.color_qr = self.form.cleaned_data['color_qr']
                    create_new_qr.bg_color_qr = self.form.cleaned_data['bg_color_qr']
                    create_new_qr.border_color_qr = self.form.cleaned_data['border_color_qr']
                    create_new_qr.border_qr = self.form.cleaned_data['border_qr']
                    create_new_qr.type_app = 'qr'
                    create_new_qr.save()

                    messages.success(
                        self.request, 'The QR Code has been created')
                    return redirect('dashboard')

            if bool(short_url_form):
                if check_short_url_link(short_url_form) == False and check_short_url_qr(short_url_form) == False:
                    create_new_qr = ModelQR()
                    create_new_qr.user = self.request.user.email
                    create_new_qr.original_url = self.form.cleaned_data['original_url']
                    create_new_qr.title = self.getting_title_window()
                    create_new_qr.short_url = short_url_form
                    create_new_qr.color_qr = self.form.cleaned_data['color_qr']
                    create_new_qr.bg_color_qr = self.form.cleaned_data['bg_color_qr']
                    create_new_qr.border_color_qr = self.form.cleaned_data['border_color_qr']
                    create_new_qr.border_qr = self.form.cleaned_data['border_qr']
                    create_new_qr.type_app = 'qr'
                    create_new_qr.save()
                    messages.success(
                        self.request, 'The QR Code has been created')
                    return redirect('dashboard')

            if bool(short_url_form):
                if check_short_url_link(short_url_form) or check_short_url_qr(short_url_form):
                    messages.error(
                        self.requests, 'This custom back-half is already exists. Try another one')
                    return redirect('create_new_qr_codes')

        except:
            messages.error(
                self.request, 'Verify if you have copied correctly the url you want to shorten')
            return redirect('create_new_qr_codes')
