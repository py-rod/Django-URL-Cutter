from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SaveUrlShortened
import string
import random
from django.contrib import messages
from .forms import CreateUrlShort

# Create your views here.


@login_required(login_url='signin')
def create_url_link(request):
    if request.method == 'POST':
        form = CreateUrlShort(request.POST)
        if form.is_valid():
            try:
                create_new_url = SaveUrlShortened()
                create_new_url.user = request.user.email
                create_new_url.original_url = form.cleaned_data['original_url']
                create_new_url.title = form.cleaned_data['title']
                create_new_url.short_url = form.cleaned_data['short_url']
                create_new_url.save(request.scheme)

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
