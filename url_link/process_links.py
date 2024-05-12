from django.contrib import messages
from .models import ModelUrl
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from qr_codes_link.models import ModelQR
import random
import string


def check_short_url_qr(short_url):
    return ModelQR.objects.filter(short_url=short_url).exists()


def check_short_url_link(short_url):
    return ModelUrl.objects.filter(short_url=short_url).exists()


def generate_short_url():
    random_digits_for_ur = ''.join(random.choices(
        f'{string.ascii_lowercase}{string.ascii_uppercase}{string.digits}', k=8))

    return f'{random_digits_for_ur}'


# ESTA CLASE SIRVE PARA GUARDAR LA URL CUANDO EL TITULO ESTA PERSONALIZADO, OSEA NO ESTA VACIO
class TitleIsNotNone:
    def __init__(self, request, form) -> None:
        self.request = request
        self.form = form

    def getting_icon_site(self):
        try:
            url = self.form.cleaned_data['original_url']
            parts = url.split('/')
            url_domain = parts[0] + '//' + parts[2] + '/'

            response = requests.get(url_domain)
            soup = BeautifulSoup(response.text, 'html.parser')
            favicon_link = soup.find('link', rel='icon')

            if favicon_link is not None:
                favicon_url = favicon_link['href']
                if not favicon_url.startswith('http'):
                    favicon_url = url_domain + favicon_url
                return favicon_url
            return url_domain + 'favicon.ico'
        except:
            return '../media/default/icon_broken.webp'

    def save_when_title_is_not_none(self):
        try:
            # SHORT URL DEL FORM
            short_url_form = self.form.cleaned_data['short_url']

            # CONDICION SI EL SHORT URL VIENE VACIO
            if bool(short_url_form) == False:

                new_short_url = generate_short_url()

                if check_short_url_link(new_short_url) == False and check_short_url_qr(new_short_url) == False:

                    create_new_url = ModelUrl()
                    create_new_url.user = self.request.user.email
                    create_new_url.original_url = self.form.cleaned_data['original_url']
                    create_new_url.title = self.form.cleaned_data['title']
                    create_new_url.short_url = new_short_url
                    create_new_url.icon = self.getting_icon_site()
                    create_new_url.type_app = 'url'
                    create_new_url.save()

                    messages.success(
                        self.request, 'The url short has been created')
                    return redirect('dashboard')

                elif check_short_url_link(new_short_url) or check_short_url_qr(new_short_url):

                    create_new_url = ModelUrl()
                    create_new_url.user = self.request.user.email
                    create_new_url.original_url = self.form.cleaned_data['original_url']
                    create_new_url.title = self.form.cleaned_data['title']
                    while check_short_url_link(new_short_url) or check_short_url_qr(new_short_url):
                        create_new_url.short_url = generate_short_url()
                    create_new_url.icon = self.getting_icon_site()
                    create_new_url.type_app = 'url'
                    create_new_url.save()

                    messages.success(
                        self.request, 'The url short has been created')
                    return redirect('dashboard')

            if bool(short_url_form):

                if check_short_url_link(short_url_form) == False and check_short_url_qr(short_url_form) == False:
                    create_new_url = ModelUrl()
                    create_new_url.user = self.request.user.email
                    create_new_url.original_url = self.form.cleaned_data['original_url']
                    create_new_url.title = self.form.cleaned_data['title']
                    create_new_url.short_url = short_url_form
                    create_new_url.icon = self.getting_icon_site()
                    create_new_url.type_app = 'url'
                    create_new_url.save()

                    messages.success(
                        self.request, 'The url short has been created')
                    return redirect('dashboard')

            if bool(short_url_form):

                if check_short_url_qr(short_url_form) or check_short_url_qr(short_url_form):
                    messages.error(
                        self.requests, 'This custom back-half is already exists. Try another one')
                    return redirect('create_url')

        except:
            messages.error(
                self.request, 'Verify if you have copied correctly the url you want to shorten')
            return redirect('create_url')


# ESTA CLASE SIRVE PARA GUARDAR LA URL CUANDO EL TITULO ESTA VACIO
class TitleIsNone:
    def __init__(self, request, form) -> None:
        self.request = request
        self.form = form

    def getting_icon_site(self):
        try:
            url = self.form.cleaned_data['original_url']
            parts = url.split('/')
            url_domain = parts[0] + '//' + parts[2] + '/'

            response = requests.get(url_domain)
            soup = BeautifulSoup(response.text, 'html.parser')
            favicon_link = soup.find('link', rel='icon')

            if favicon_link is not None:
                favicon_url = favicon_link['href']
                if not favicon_url.startswith('http'):
                    favicon_url = url_domain + favicon_url
                return favicon_url
            return url_domain + 'favicon.ico'
        except:
            return '../media/default/icon_broken.webp'

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

                    create_new_url = ModelUrl()
                    create_new_url.user = self.request.user.email
                    create_new_url.original_url = self.form.cleaned_data['original_url']
                    create_new_url.title = self.getting_title_window()
                    create_new_url.short_url = new_short_url
                    create_new_url.icon = self.getting_icon_site()
                    create_new_url.type_app = 'url'
                    create_new_url.save()

                    messages.success(
                        self.request, 'The url short has been created')
                    return redirect('dashboard')

                elif check_short_url_link(new_short_url) or check_short_url_qr(new_short_url):

                    create_new_url = ModelUrl()
                    create_new_url.user = self.request.user.email
                    create_new_url.original_url = self.form.cleaned_data['original_url']
                    create_new_url.title = self.getting_title_window()
                    while check_short_url_link(new_short_url) or check_short_url_qr(new_short_url):
                        create_new_url.short_url = generate_short_url()
                    create_new_url.icon = self.getting_icon_site()
                    create_new_url.save()
                    messages.success(
                        self.request, 'The url short has been created')
                    return redirect('dashboard')

            if bool(short_url_form):

                if check_short_url_link(short_url_form) == False and check_short_url_qr(short_url_form) == False:
                    create_new_url = ModelUrl()
                    create_new_url.user = self.request.user.email
                    create_new_url.original_url = self.form.cleaned_data['original_url']
                    create_new_url.title = self.getting_title_window()
                    create_new_url.short_url = short_url_form
                    create_new_url.icon = self.getting_icon_site()
                    create_new_url.type_app = 'url'
                    create_new_url.save()

                    messages.success(
                        self.request, 'The url short has been created')
                    return redirect('dashboard')

                else:
                    messages.error(
                        self.requests, 'This custom back-half is already exists. Try another one')
                    return redirect('create_url')

        except:
            messages.error(
                self.request, 'Verify if you have copied correctly the url you want to shorten')
            return redirect('create_url')
