from django.contrib import messages
from .models import SaveUrlShortened
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect


# Guardando cuando el titulo del link no esta en blanco
def save_when_title_is_not_none(request, form):
    try:
        create_new_url = SaveUrlShortened()
        create_new_url.user = request.user.email
        create_new_url.original_url = form.cleaned_data['original_url']
        create_new_url.title = form.cleaned_data['title']
        create_new_url.short_url = form.cleaned_data['short_url']
        create_new_url.save()

        messages.success(request, 'The url short has been created')
        return redirect('dashboard')
    except:
        messages.error(
            request, 'Verify if you have copied correctly the url you want to shorten')
        return redirect('create_url')


# Guardando cuando el titulo del link esta vacio
def save_when_title_is_none(request, form):
    # Si no introdujo nada, hacemos una peticion para obtener el titulo de la ventana del link a guardar
    response = requests.get(form.cleaned_data['original_url'])
    # Si el status es exitoso hacemos la transformacion
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        window_title = soup.title.string
        try:
            create_new_url = SaveUrlShortened()
            create_new_url.user = request.user.email
            create_new_url.original_url = form.cleaned_data['original_url']
            create_new_url.title = window_title
            create_new_url.short_url = form.cleaned_data['short_url']
            create_new_url.save()

            messages.success(
                request, 'The url short has been created')
            return redirect('dashboard')
        except:
            messages.error(
                request, 'Verify if you have copied correctly the url you want to shorten')
            return redirect('create_url')

    else:
        messages.error(
            request, 'Verify if you have copied correctly the url you want to shorten')
        return redirect('create_url')
