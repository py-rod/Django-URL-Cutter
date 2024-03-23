from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import SaveUrlShortened
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from .forms import CreateUrlShort

# Create your views here.


@login_required(login_url='signin')
def create_url_link(request):
    domain = get_current_site(request).domain
    if request.method == 'POST':
        form = CreateUrlShort(request.POST)
        if form.is_valid():
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
                    request, 'There was a problem with your custom url, write another one')
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


def all_url_links(request):

    urls_obj = SaveUrlShortened.objects.filter(user=request.user.email)
    domain = get_current_site(request).domain

    return render(request, 'all_url_links.html', {
        'data_urls': urls_obj,
        'domain': domain
    })
