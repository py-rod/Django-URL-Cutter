from django.shortcuts import render
from url_link.models import ModelUrl
from qr_codes_link.models import ModelQR
from .models import UrlAnalytics, QRAnalytics
from django.contrib.sites.shortcuts import get_current_site
from .count_devices import *
from django.db.models import Count

# Create your views here.


def analytics(request):
    # URL
    popular_click = ModelUrl.objects.all().order_by('-clicks').first()
    url_popular_system = UrlAnalytics.objects.values('system').annotate(
        total=Count('system')).order_by('-total')
    url_popular_browser = UrlAnalytics.objects.values('browser').annotate(
        total=Count('browser')).order_by('-total')
    # QR
    popular_qr_code = ModelQR.objects.all().order_by('-scans').first()
    qr_popular_system = QRAnalytics.objects.values('system').annotate(
        total=Count('system')).order_by('-total')
    qr_popular_browser = QRAnalytics.objects.values('browser').annotate(
        total=Count('browser')).order_by('-total')

    get_domain = get_current_site(request).domain

    if bool(url_popular_system) and bool(qr_popular_system):
        return render(request, 'analytics.html', {
            'click': popular_click,
            'scan': popular_qr_code,
            'domain': get_domain,
            'url_popular_system': url_popular_system[0]['system'],
            'url_popular_browser': url_popular_browser[0]['browser'],
            'url_mobile': url_is_mobile(),
            'url_pc': url_is_pc(),
            'url_tablet': url_is_tablet(),
            'url_other': url_other(),
            'qr_popular_system': qr_popular_system[0]['system'],
            'qr_popular_browser': qr_popular_browser[0]['browser'],
            'qr_mobile': qr_is_mobile(),
            'qr_pc': qr_is_pc(),
            'qr_tablet': qr_is_tablet(),
            'qr_other': qr_other()
        })

    if bool(url_popular_system) and bool(qr_popular_system) == False:
        return render(request, 'analytic_link.html', {
            'click': popular_click,
            'domain': get_domain,
            'url_popular_system': url_popular_system[0]['system'],
            'url_popular_browser': url_popular_browser[0]['browser'],
            'url_mobile': url_is_mobile(),
            'url_pc': url_is_pc(),
            'url_tablet': url_is_tablet(),
            'url_other': url_other(),
        })

    if bool(qr_popular_system) and bool(url_popular_system) == False:
        return render(request, 'analytic_qr.html', {
            'scan': popular_qr_code,
            'domain': get_domain,
            'qr_popular_system': qr_popular_system[0]['system'],
            'qr_popular_browser': qr_popular_browser[0]['browser'],
            'qr_mobile': qr_is_mobile(),
            'qr_pc': qr_is_pc(),
            'qr_tablet': qr_is_tablet(),
            'qr_other': qr_other()
        })

    if bool(url_popular_system) == False and bool(qr_popular_system) == False:
        return render(request, 'not_found.html')
