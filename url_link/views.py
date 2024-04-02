from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import SaveUrlShortened
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from .forms import CreateUrlShort
import requests
from bs4 import BeautifulSoup
from .process_links import TitleIsNotNone, TitleIsNone
# Create your views here.


@login_required(login_url='signin')
def all_url_links(request):

    urls_obj = SaveUrlShortened.objects.filter(
        user=request.user.email, is_active=True)
    domain = get_current_site(request).domain

    return render(request, 'all_url_links.html', {
        'data_urls': urls_obj,
        'domain': domain
    })


@login_required(login_url='signin')
def create_url_link(request):
    if request.method == 'POST':
        form = CreateUrlShort(request.POST)
        if form.is_valid():
            # Viendo si el usuario introdujo un titulo a la url
            window_title = form.cleaned_data['title']
            if window_title:
                return TitleIsNotNone(request, form).save_when_title_is_not_none()
            else:
                return TitleIsNone(request, form).save_when_title_is_none()
        else:
            messages.error(
                request, 'This custom back-half is already exists. Try another one')
            return redirect('create_url')

    else:
        form = CreateUrlShort()
    return render(request, 'create_url.html', {
        'form': form
    })


def redirect_urls(request, short_url):
    try:
        url_obje = SaveUrlShortened.objects.get(short_url=short_url)
        print(url_obje)
        url_obje.clicks += 1
        url_obje.save()
        return redirect(url_obje.original_url)
    except SaveUrlShortened.DoesNotExist:
        return HttpResponse('No existe la url acortada')
