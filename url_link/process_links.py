from django.contrib import messages
from .models import SaveUrlShortened
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect


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
            icon = self.getting_icon_site()
            create_new_url = SaveUrlShortened()
            create_new_url.user = self.request.user.email
            create_new_url.original_url = self.form.cleaned_data['original_url']
            create_new_url.title = self.form.cleaned_data['title']
            create_new_url.short_url = self.form.cleaned_data['short_url']
            create_new_url.icon = icon
            create_new_url.save()

            messages.success(self.request, 'The url short has been created')
            return redirect('dashboard')
        except:
            messages.error(
                self.request, 'Verify if you have copied correctly the url you want to shorten')
            return redirect('create_url')


# ESTA CLASE SIRVE PARA GUARDAR LA URL CUANDO EL TITULO NO ESTA VACIO Y ESTA PERSONALIZADO
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
        # Si no introdujo nada, hacemos una peticion para obtener el titulo de la ventana del link a guardar
        try:
            create_new_url = SaveUrlShortened()
            create_new_url.user = self.request.user.email
            create_new_url.original_url = self.form.cleaned_data['original_url']
            create_new_url.title = self.getting_title_window()
            create_new_url.short_url = self.form.cleaned_data['short_url']
            create_new_url.icon = self.getting_icon_site()
            create_new_url.save()

            messages.success(
                self.request, 'The url short has been created')
            return redirect('dashboard')
        except:
            messages.error(
                self.request, 'Verify if you have copied correctly the url you want to shorten')
            return redirect('create_url')
