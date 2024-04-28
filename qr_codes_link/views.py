from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreateQRCodeForm
from .models import QRGenerator
from .process_qr_codes import TitleIsNone, TitleIsNotNone
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from analytics.models import QRAnalytics
# Create your views here.


@login_required(login_url='signin')
def all_qr_codes(request):

    qr_codes = QRGenerator.objects.all()

    domain = get_current_site(request).domain

    return render(request, 'all_qr_codes.html', {
        'qr_codes': qr_codes,
        'domain': f'{domain}/',
        'pleca': '/'
    })


@login_required(login_url='signin')
def create_qr_codes(request):
    if request.method == 'POST':
        form = CreateQRCodeForm(request.POST)
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
        form = CreateQRCodeForm()
    return render(request, 'create_qr_codes.html', {
        'form': form,
    })


def redirect_qr_codes(request, short_url):
    try:
        # URLS ANALYTICS CREATION
        create_analytics = QRAnalytics()
        create_analytics.id_short_url = short_url
        create_analytics.is_mobile = request.user_agent.is_mobile
        create_analytics.is_tablet = request.user_agent.is_tablet
        create_analytics.is_pc = request.user_agent.is_pc
        create_analytics.is_touch_capable = request.user_agent.is_touch_capable
        create_analytics.is_bot = request.user_agent.is_bot
        create_analytics.browser = request.user_agent.browser.family
        create_analytics.system = request.user_agent.os.family
        create_analytics.device = request.user_agent.device.family
        create_analytics.save()

        # SAVE THE NUMBER OF SCANS WHEN THE USER SCANS ON THE LINK
        qr_object = QRGenerator.objects.get(
            short_url=short_url)
        qr_object.scans += 1
        qr_object.save()
        return redirect(qr_object.original_url)
    except QRGenerator.DoesNotExist:
        return HttpResponse('No existe el codigo qr')
